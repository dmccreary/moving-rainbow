// Function to add copy buttons to prompt admonitions
function addCopyButtonsToPrompts() {
    // Find all admonitions with the "prompt" class
    document.querySelectorAll(".admonition.prompt").forEach((admonition) => {
        // Skip if button already added
        if (admonition.querySelector(".copy-button")) {
            return;
        }

        // Create a "Copy" button
        const copyButton = document.createElement("button");
        copyButton.textContent = "Copy";
        copyButton.className = "copy-button";

        // Append the button to the admonition
        admonition.appendChild(copyButton);

        // Add event listener for the button
        copyButton.addEventListener("click", () => {
            // Collect all text content inside the admonition except the title and button
            const promptText = Array.from(admonition.querySelectorAll("p:not(.admonition-title)"))
                .map((p) => p.textContent.trim())
                .join("\n");

            if (promptText) {
                // Copy the collected text to the clipboard
                navigator.clipboard.writeText(promptText).then(
                    () => {
                        // Show feedback on successful copy
                        copyButton.textContent = "Copied!";
                        setTimeout(() => (copyButton.textContent = "Copy"), 2000);
                    },
                    (err) => {
                        console.error("Failed to copy text: ", err);
                    }
                );
            } else {
                console.error("No prompt text found to copy.");
            }
        });
    });
}

// Run on DOMContentLoaded
document.addEventListener("DOMContentLoaded", addCopyButtonsToPrompts);

// Also run after navigation for Material theme's instant loading
if (typeof document$ !== "undefined") {
    document$.subscribe(addCopyButtonsToPrompts);
}