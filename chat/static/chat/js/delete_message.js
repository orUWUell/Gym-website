async function deleteMessage(messageId, userId) {
    let response = await fetch(`/chat/delete/${messageId}/${userId}`,
        {
            method: 'get',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json'
            },
        }).then(response => response.json())
    .then(data => {
        message = document.getElementById(`message-${messageId}`)
        message.

    }
    )

}
