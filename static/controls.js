/* ================================================
   CONFIGURATION – Remplace les IPs et endpoints ici
================================================ */
const DEVICES = {
    porte: {
        ip: "10.0.0.239",
        actions: {
            on:  "/PORTE=ON",
            off: "/PORTE=OFF",
        }
    },
    pompe: {
        ip: "10.0.0.239",
        actions: {
            on:  "/POMPE=ON",
            off: "/POMPE=OFF",
        }
    },
    fan: {
        ip: "10.0.0.129",
        actions: {
            low:    "/power?level=1",
            medium: "/power?level=2",
            high:   "/power?level=3",
            off:    "/power?level=0",
        }
    },
    valves: {
        ip: "10.0.0.13",
        actions: {
            "valve 1": "/VALVE1=ON",
            "valve 2": "/VALVE2=ON",
            "valve 3": "/VALVE3=ON",
            off:       "/VALVES=OFF",
        }
    },
};

/* ================================================
   UTILITAIRE – Envoie une requête GET au module
================================================ */
function sendRequest(ip, endpoint) {
    const url = `http://${ip}${endpoint}`;
    console.log("GET →", url);
    fetch(url).catch(err => console.error(`Erreur [${url}] :`, err));
}

/* ================================================
   INITIALISATION
================================================ */
document.addEventListener("DOMContentLoaded", () => {

    /* ── Slider – affichage valeur ── */
    const slider    = document.getElementById("wateringTime");
    const valueSpan = document.getElementById("wateringValue");
    if (slider && valueSpan) {
        valueSpan.textContent = slider.value;
        slider.addEventListener("input", () => {
            valueSpan.textContent = slider.value;
        });
    }

    /* ── Mode AUTO / MANUEL ── */
    const modeButtons    = document.querySelectorAll(".mode-btn");
    const manualControls = document.querySelectorAll(
        ".toggle-btn, .exclusive-btn, input[type='range']"
    );

    function applyModeState() {
        const activeBtn = document.querySelector(".mode-btn.active");
        const isAuto    = activeBtn?.dataset.mode === "auto";
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

    applyModeState(); // Appliquer l'état AUTO au chargement

    /* ── ON / OFF (porte, pompe) ── */
    document.querySelectorAll(".toggle-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("disabled")) return;

            const group   = btn.dataset.group;
            const actionKey = btn.classList.contains("btn-on") ? "on" : "off";
            const device  = DEVICES[group];

            // Mise à jour visuelle
            document.querySelectorAll(`.toggle-btn[data-group="${group}"]`)
                .forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            // Envoi requête
            if (device) sendRequest(device.ip, device.actions[actionKey]);
        });
    });

    /* ── Groupes exclusifs (fan, valves) ── */
    document.querySelectorAll(".exclusive-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("disabled")) return;

            const group     = btn.dataset.group;
            const label     = btn.textContent.trim().toLowerCase();
            const device    = DEVICES[group];
            const actionKey = device?.actions[label] ? label : "off";

            // Mise à jour visuelle
            document.querySelectorAll(`.exclusive-btn[data-group="${group}"]`)
                .forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            // Envoi requête + temps d'arrosage pour les valves
            if (device) {
                let endpoint = device.actions[actionKey];
                if (group === "valves" && actionKey !== "off" && slider) {
                    endpoint += `&duration=${slider.value}`;
                }
                sendRequest(device.ip, endpoint);
            }
        });
    });

});


