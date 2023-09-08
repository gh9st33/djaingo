```javascript
// Establish a WebSocket connection
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
);

// DOM elements
const chatComponent = document.querySelector('#chatComponent');
const workspaceComponent = document.querySelector('#workspaceComponent');

// Event listener for incoming WebSocket messages
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if (data.message_type === 'chatMessage') {
        // Update chat component with new message
        chatComponent.innerHTML += ('<br>' + data.message);
    } else if (data.message_type === 'taskUpdate') {
        // Update workspace component with task update
        workspaceComponent.innerHTML += ('<br>' + data.message);
    }
};

// Event listener for WebSocket errors
chatSocket.onerror = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Function to send chat messages
function sendChatMessage(message) {
    chatSocket.send(JSON.stringify({
        'message_type': 'chatMessage',
        'message': message
    }));
}

// Function to send task requests
function sendTaskRequest(task) {
    chatSocket.send(JSON.stringify({
        'message_type': 'taskRequest',
        'task': task
    }));
}
```