      const roomId = JSON.parse(document.getElementById('room-id').textContent)
      const userName = JSON.parse(document.getElementById('json-username').textContent);
      const userId = JSON.parse(document.getElementById('user-id').textContent)
      const profilePicture = JSON.parse(document.getElementById('profile-picture').textContent);
      let delete_msg
      let url = `ws://${window.location.host}/ws/chat/${roomId}/`
      var form_data = new FormData();
      const chatSocket = new WebSocket(url)
      var currentdate = new Date();
      var today = currentdate.getDate() + "/" +
          (currentdate.getMonth() + 1) + "/" +
          currentdate.getFullYear() + " " +
          currentdate.getHours() + ":" +
          currentdate.getMinutes() + ":" +
          currentdate.getSeconds();
      function delete_button_func (message_id) {
          delete_msg = message_id
      }
      delete_form = document.getElementById("delete-form")
      delete_form.addEventListener('submit', (e) => {
          e.preventDefault()
          chatSocket.send(JSON.stringify({
              'action': 'delete',
              'message': delete_msg
          }))

      })
      chatSocket.onmessage = function(e) {
          let data = JSON.parse(e.data)
          console.log('Data:', data)

          if (data.type === 'send') {
              let messages = document.getElementById('messages')
              messages.insertAdjacentHTML('beforeend',
                  `<div class="bubbleWrapper">
        <div class="photo">
            <p><img src="${data.profile_picture}" width="150" height="150"></p>
        </div>
		<div class="text_message">
<!--		{# КОСТЫЛЬЬЬЬ ОБРАТИ ВНИМАНИЕ И ПОЧИНИ НОРМАЛЬНО #}-->

            <h1><a href="http://127.0.0.1:8000/users/profile/${data.userid}">${data.author}</a></h1>

            <p align="left" class="message">${data.message}</p>
        </div>
        </div><span class="date">${today}</span>
         <hr>`)
          } else if (data.type === 'delete') {
              message = document.getElementById(`message-${data.message}`)
              message.remove()
          }
      }

      let form = document.getElementById('form')
      let inpFile = document.getElementById("file-input")
      form.addEventListener('submit', (e) => {
          e.preventDefault()
          file = inpFile.files[0]

          let message = e.target.message.value
          chatSocket.send(JSON.stringify({
              'message': message,
              'username': userName,
              'datetime': today,
              'user_id': userId,
              'profile_picture': profilePicture,
              'action': 'send'
          }))
          form.reset()
      })

      $.ajax({
          type: "POST",
          url: "{% url 'chat' room.id %}",
          data: {
              message: $('#message').val(),
              csrf

          }
      })