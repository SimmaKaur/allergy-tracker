// Display allergic ingredients in the popup
chrome.runtime.onMessage.addListener(function(allergicIngredients) {
    let ul = document.getElementById('allergicIngredients');
    allergicIngredients.forEach(function(ingredient) {
      let li = document.createElement('li');
      li.textContent = ingredient;
      ul.appendChild(li);
    });
  });
  
  // Fetch allergic ingredients from background script
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getIngredients" });
  });
  
  
  
  