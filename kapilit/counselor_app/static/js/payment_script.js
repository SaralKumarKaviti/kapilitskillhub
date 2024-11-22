function showProceedButton(selectedRadio) {
    const proceedButton = document.getElementById("proceed-btn");
    const offlineLabel = document.getElementById("label-offline");
    const onlineLabel = document.getElementById("label-online");

    // Display the "Proceed to Payment" button
    proceedButton.style.display = "block";

    // Update label colors based on selection
    if (selectedRadio.id === "offline") {
        offlineLabel.classList.add("selected"); // Apply orange color
        onlineLabel.classList.remove("selected");
    } else if (selectedRadio.id === "online") {
        onlineLabel.classList.add("selected"); // Apply orange color
        offlineLabel.classList.remove("selected");
    }
}
