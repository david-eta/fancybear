// static/js/remove_button.js
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
