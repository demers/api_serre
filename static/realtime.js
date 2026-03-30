// ─────────────────────────────────────────────────────
// Remplir le tableau avec les données de /moniteur
// ─────────────────────────────────────────────────────
async function actualiserTableau() {

    const reponse = await fetch('/moniteur');
    const json    = await reponse.json();
    const capteurs = json["Temperatures et humidites des capteurs 1, 2 et 3"];

    // Fonction utilitaire pour formater l'heure
    function formaterDate(dateStr) {
        return new Date(dateStr).toLocaleTimeString('fr-CA', {
            hour:   '2-digit',
            minute: '2-digit',
            second: '2-digit',
            timeZone: 'UTC'
        });
    }

    // Capteur 1 → Température Haut
    document.getElementById('sensor-temp-haut').textContent = capteurs["1"].Temperature + ' °C';
    document.getElementById('time-temp-haut').textContent   = formaterDate(capteurs["1"].Date);

    // Capteur 2 → Température Bas
    document.getElementById('sensor-temp-bas').textContent  = capteurs["3"].Temperature + ' °C';
    document.getElementById('time-temp-bas').textContent    = formaterDate(capteurs["3"].Date);

    // Capteur 3 → Température Extérieur
    document.getElementById('sensor-temp-ext').textContent  = capteurs["2"].Temperature + ' °C';
    document.getElementById('time-temp-ext').textContent    = formaterDate(capteurs["2"].Date);

    // Humidité → vient du capteur 1 (le seul qui a Humidite dans ton JSON)
    const humidite = capteurs["1"].Humidite;
    document.getElementById('sensor-humidite').textContent  = humidite !== undefined ? humidite + ' %' : '-- %';
    document.getElementById('time-humidite').textContent    = formaterDate(capteurs["1"].Date);
}

// Lancer au chargement, puis toutes les 5 minutes
// (plus fréquent que les graphiques car c'est du "real time")
document.addEventListener('DOMContentLoaded', function() {
    actualiserTableau();
    setInterval(actualiserTableau, 5 * 60 * 1000);
});