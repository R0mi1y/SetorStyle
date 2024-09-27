function showPopup(title, message, buttons) {
    console.log(title, message, buttons);
    
    const $popup = $("#custom-popup");
    const $popupTitle = $("#popup-title");
    const $popupMessage = $("#popup-message");
    const $popupButtons = $("#popup-buttons");

    if (title) {
        $popupTitle.text(title);
    } else {
        $popupTitle.text("");
    }

    $popupMessage.text(message);

    $popupButtons.empty();

    if (buttons && Array.isArray(buttons)) {
        $.each(buttons, function(index, button) {
            const $btn = $("<button class='btn-submit'>").text(button.text);

            if (button.action) {
                $btn.on("click", function() {
                    button.action();
                    closePopup();
                });
            }

            $popupButtons.append($btn);
        });
    }

    $popup.css("display", "flex");
}

function closePopup() {
    $("#custom-popup").css("display", "none");
}
