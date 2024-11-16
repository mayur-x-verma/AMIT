document.getElementById('subscription-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way
    const fullName = document.getElementById('full-name').value;
    const email = document.getElementById('email').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
    // Show loading spinner
    document.getElementById('loading-spinner').classList.remove('hidden');
  
    fetch(subscribeUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
      body: JSON.stringify({
        full_name: fullName,
        email: email
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        document.getElementById('popup-text').textContent = "Subscription successful!";
      } else {
        document.getElementById('popup-text').textContent = `An error occurred: ${data.error}`;
      }
      document.getElementById('popup-message').classList.remove('hidden');
    })
    .catch(error => {
      document.getElementById('popup-text').textContent = "An error occurred. Please try again.";
      document.getElementById('popup-message').classList.remove('hidden');
    })
    .finally(() => {
      // Hide loading spinner
      document.getElementById('loading-spinner').classList.add('hidden');
    });
  });
  
  document.getElementById('popup-close').addEventListener('click', function() {
    document.getElementById('popup-message').classList.add('hidden');
  });
  