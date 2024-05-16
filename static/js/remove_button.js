/*
  JavaScript Function for Setting up Removal Buttons:

  - Function setupRemovalButtons: Sets up removal buttons for elements matching a given class.
    Parameters:
      - button_class: CSS class selector for removal buttons.
      - removal_url: URL to send removal request.
      - parent_class: CSS class selector for parent element to remove.
      - data_identifier: Attribute name to identify the data associated with the element.

  - The function attaches a click event listener to each button matching the provided class.
    When clicked, it prevents event propagation, sends a POST request to the removal URL
    with necessary data (including CSRF token), and removes the parent element upon successful removal.
    If there's an issue with removal, it displays an alert message.
*/

function setupRemovalButtons(button_class, removal_url, parent_class, data_identifier) {
  document.querySelectorAll(button_class).forEach(img => {
    img.addEventListener('click', function(event) {
      event.stopPropagation(); // Prevent the click from affecting parent elements
          
      const identifier = this.getAttribute(data_identifier);
      const data = {'stock': identifier};
      fetch(removal_url, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // fetch the CSRF token
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          this.closest(parent_class).remove();
        } else {
          alert("There was a problem with the removal.");
        }
      });
    });
  });
}
