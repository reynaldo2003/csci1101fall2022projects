window.addEventListener("load", function ()
{
    // Get click elements.
    let clickButtonElement = document.getElementById("click_button");
    let clickCounterElement = document.getElementById("click_counter");
    
    // Counter Value
    let counter = 0;

    // Button click function.
    let clickButtonFunction = function ()
    {
        //Increment counter.
        counter++;

        // Update click counter text
        clickCounterElement.innerHTML = counter;
    };

    // Attached click function to button.
    clickButtonElement.addEventListener("click", clickButtonFunction);
});