// Function to scrape ingredients from the page
function scrapeIngredients() {
    let ingredients = [];
    // Replace this selector with the actual selector for ingredients on the page
    let ingredientElements = document.querySelectorAll('.ingredient-list li');
    ingredientElements.forEach(element => {
      ingredients.push(element.textContent.trim());
    });
    return ingredients;
  }
  
  // Send ingredients to background script
  chrome.runtime.sendMessage({ ingredients: scrapeIngredients() });
  
  
  
  