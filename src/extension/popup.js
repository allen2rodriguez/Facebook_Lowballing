// Build out a simple extension that when clicked on will start to run all the files and get the information
// I also would like it to display the messages that would be sent out to the console and have the ability to give it an ok

let button = document.getElementById('activate_button');
button.addEventListener('click', sendPostRequest);

/**
 * This function is called when the button is clicked.
 * @param {string} url - The URL to send the POST request to.
 * @returns {void}
 */
function sendPostRequest() {
    fetch('http://127.0.0.1:5000/main')
        .then(response => response.json())
        .then(data => {
            console.log('Response from python:', data);
            alert(JSON.stringify(data.messages)); // or adjust as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
}