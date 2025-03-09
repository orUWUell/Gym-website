      const roomId = JSON.parse(document.getElementById('room-id').textContent)
      const userName = JSON.parse(document.getElementById('json-username').textContent);
      const userId = JSON.parse(document.getElementById('user-id').textContent)
      const profilePicture = JSON.parse(document.getElementById('profile-picture').textContent);
      let delete_msg
      let url = `ws://${window.location.host}/ws/chat/${roomId}/`
      const chatSocket = new WebSocket(url)
      var currentdate = new Date();

      function toDataURL(file) {
          return new Promise((resolve, reject) => {
              const reader = new FileReader();
              reader.onload = () => resolve(reader.result); // Возвращаем dataURL
              reader.onerror = () => reject(reader.error); // Возвращаем ошибку
              reader.readAsDataURL(file); // Начинаем чтение файла
          });
      }

      // Асинхронная функция для использования toDataURL

      var today = currentdate.getDate() + "/" +
          (currentdate.getMonth() + 1) + "/" +
          currentdate.getFullYear() + " " +
          currentdate.getHours() + ":" +
          currentdate.getMinutes() + ":" +
          currentdate.getSeconds();

      function delete_button_func(message_id) {
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

      // Отправка сообщения на фронтенд
      chatSocket.onmessage = function(e) {
          let data = JSON.parse(e.data)
          let delete_button
          if (userId === data.userid) {
              delete_button =
                  `<button type="submit" class="trash-button" onclick="delete_button_func(${data.message_id})">  <svg class="trash-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
    <path d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/>
  </svg>
  Удалить</button>`
          } else delete_button = ``
          if (data.type === 'send') {
              let messages = document.getElementById('messages')
              let file
              if (data.file_name) {
                file = `&#x1F4CE; <a class="cursor-pointer italic hover:underline" href="${data.file}" download>${data.file_name}</a>`
              } else file = ``
              messages.insertAdjacentHTML('beforeend',
                  `
<div id="message-${data.message_id}">
<div class="bubbleWrapper">
        <div class="photo">
            <p><img src="${data.profile_picture}" width="150" height="150"></p>
        </div>
		<div class="text_message">

            <h1><a href="http://127.0.0.1:8000/users/profile/${data.userid}">${data.author}</a></h1>

            <p align="left" class="message">${data.message}</p>
            ${file}
        </div>
        ${delete_button}
        </div><span class="date">${today}</span>
         <hr>
</div>`)
          } else if (data.type === 'delete') {

              let message = document.getElementById(`message-${data.message}`)
              message.remove()
          }
      }

      //Отправка сооббщений на сервер
      let form = document.getElementById('form')
      form.addEventListener('submit', async (e) => {
          e.preventDefault();

          let file = e.target.file_input.files[0]; // Инициализируем переменную fileURL
          let message = e.target.message.value; // Получаем значение текстового сообщения

          // Проверяем, есть ли файл
          if (file) {
              try {
                  // Читаем файл и получаем dataURL
                  fileURL = await toDataURL(file);
                  file = {
                      'name': file.name,
                      'type': file.type,
                      'bytes': fileURL
                  }
                  // Выводим fileURL
              } catch (error) {
                  console.error('Error reading file:', error); // Обрабатываем ошибку
              }
          } else file = null

          // Отправляем данные через WebSocket
          chatSocket.send(JSON.stringify({
              'message': message,
              'username': userName,
              'datetime': today,
              'user_id': userId,
              'profile_picture': profilePicture,
              'file': file, // Используем fileURL (может быть null)
              'action': 'send'
          }));

          // Сбрасываем форму после отправки
          form.reset();
      });
      // ajax связь
      $.ajax({
          type: "POST",
          url: "{% url 'chat' room.id %}",
          contentType: false,
          processData: false,
          data: {
              message: $('#message').val(),
              csrf

          }
      })