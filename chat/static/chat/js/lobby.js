        const roomId = JSON.parse(document.getElementById('room-id').textContent)
        const userName = JSON.parse(document.getElementById('json-username').textContent)
        const userId = JSON.parse(document.getElementById('json-id').textContent)


        let url = `ws://${window.location.host}/ws/chat/${roomId}/`

        const chatSocket = new WebSocket(url)

        chatSocket.onmessage = function(e){
            let data = JSON.parse(e.data)
            console.log('Data:', data)

            if(data.type === 'chat'){
                if (data.message.trim() !== "") {
                let messages = document.getElementById('messages')
                messages.insertAdjacentHTML('beforeend',
                                    `<div class='message'>
                                        <a href="/users/profile/${data.author_id}" id='now_message'>${data.author}</a>
                                        <p>${data.message}</p>
                                    </div>`)
            }
            }
        }

        let form = document.getElementById('form')
        form.addEventListener('submit', (e)=> {
            e.preventDefault()
            let message = e.target.message.value
            chatSocket.send(JSON.stringify({
                'message':message,
                'username': userName,
                'user_id': userId
            }))
            form.reset()
        })

        $.ajax({
            type: "POST",
            url: "{% url 'chat' room.id %}",
            data: {
                message: $('#message').val(),
                csrf
        }})