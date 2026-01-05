document.addEventListener("DOMContentLoaded", () => {

    /* =========================
       SLIDER – affichage valeur
    ========================= */
    const slider = document.getElementById("wateringTime");
    const valueSpan = document.getElementById("wateringValue");

    if (slider && valueSpan) {
        valueSpan.textContent = slider.value;
        slider.addEventListener("input", () => {valueSpan.textContent = slider.value;});
    }

    /* =========================
       MODE AUTO / MANUEL
    ========================= */
    const modeButtons = document.querySelectorAll(".mode-btn");
    const manualControls = document.querySelectorAll(
        ".toggle-btn, .exclusive-btn, input[type='range']"
    );

    function applyModeState() {
        const autoBtn = document.querySelector(".mode-btn.active");
        const isAuto = autoBtn && autoBtn.dataset.mode === "auto";

        manualControls.forEach(ctrl => {
            ctrl.classList.toggle("disabled", isAuto);
            ctrl.disabled = isAuto;
        });
    }

    modeButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            modeButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            applyModeState();
        });
    });

    // ✅ Appliquer l’état AUTO dès le chargement
    applyModeState();

    /* =========================
       ON / OFF (porte, pompe)
    ========================= */
    const toggleButtons = document.querySelectorAll(".toggle-btn");

    toggleButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("disabled")) return;

            const group = btn.dataset.group;
            document
                .querySelectorAll(`.toggle-btn[data-group="${group}"]`)
                .forEach(b => b.classList.remove("active"));

            btn.classList.add("active");
        });
    });

    /* =========================
       GROUPES EXCLUSIFS
       (fan, valves)
    ========================= */
    const exclusiveButtons = document.querySelectorAll(".exclusive-btn");

    exclusiveButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("disabled")) return;

            const group = btn.dataset.group;

            // Nettoyage AVANT activation
            document
                .querySelectorAll(`.exclusive-btn[data-group="${group}"]`)
                .forEach(b => b.classList.remove("active"));

            // Activer UNIQUEMENT le bouton cliqué
            btn.classList.add("active");
        });
    });

});
