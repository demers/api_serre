const ctx   = document.getElementById('tempChart');
const state = document.getElementById('stateChart');

// ─────────────────────────────────────────────────────
// 1. APPELER L'API ET PRÉPARER LES DONNÉES
// ─────────────────────────────────────────────────────
async function chargerHistorique() {

    // Appel à la route Flask
    const reponse = await fetch('/historique24h');
    const json    = await reponse.json();

    const historique = json["Historique des capteurs 1, 2 et 3"];
    //    ^^^^^^^^^          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    //    raccourci          la clé exacte du JSON de Flask

    // Chaque capteur est un tableau d'objets, du plus récent au plus ancien.
    // .reverse() les remet dans l'ordre chronologique (gauche → droite)
    const donneesCapteur1 = historique["Capteur 1"].reverse();
    const donneesCapteur2 = historique["Capteur 2"].reverse();
    const donneesCapteur3 = historique["Capteur 3"].reverse();
    const donneesFan1 = historique["Systeme fan1"].reverse();
    const donneesFan2 = historique["Systeme fan2"].reverse();
    const donneesPompe = historique["Systeme pompe"].reverse();
    const donneesPorte = historique["Systeme porte"].reverse();
    const donneesValve1 = historique["Systeme valve1"].reverse();
    const donneesValve2 = historique["Systeme valve2"].reverse();
    const donneesValve3 = historique["Systeme valve3"].reverse();

    // ── Graphique 1 : Labels de l'axe X ────────────────────────────
    // On utilise les dates du Capteur 1 comme référence pour l'axe du temps
    // (les 3 capteurs enregistrent approximativement aux mêmes moments)
    const g1_labels = donneesCapteur1.map(function(point) {
        return new Date(point.Date).toLocaleTimeString('fr-CA', {
            hour:   '2-digit',
            minute: '2-digit',
            second: '2-digit',
            timeZone: 'UTC'
        });
        // Résultat : "12:35:03", "12:35:05", etc.
    });

    // ── Graphique 2 : Labels de l'axe X ────────────────────────────
    
    // ── Graphique 2 : format {x, y} avec string pour 'category' ──
    function extraireXY(tableau) {
        return tableau.map(function(point) {
            return {
                x: new Date(point.Date).toLocaleTimeString('fr-CA', {
                    hour:     '2-digit',
                    minute:   '2-digit',
                    second:   '2-digit',
                    timeZone: 'UTC'
                }),
                y: point.Etat
            };
        });
    }


                                            // trier chronologiquement




    // ── Températures de chaque capteur ───────────────
    // .map() parcourt chaque élément du tableau et extrait la température
    const tempCapteur1 = donneesCapteur1.map(function(point) {
        return point.Temperature;
    });

    const tempCapteur2 = donneesCapteur2.map(function(point) {
        return point.Temperature;
    });

    const tempCapteur3 = donneesCapteur3.map(function(point) {
        return point.Temperature;
    });

    const humiditeCapteur1 = donneesCapteur1.map(function(point) {
        return point.Humidite !== undefined ? point.Humidite : null;
    });

    // ── États des systèmes (0 ou 1) ───────────────────

    const etatFan1   = extraireXY(donneesFan1);
    const etatFan2   = extraireXY(donneesFan2);
    const etatPompe  = extraireXY(donneesPompe);
    const etatPorte  = extraireXY(donneesPorte);
    const etatValve1 = extraireXY(donneesValve1);
    const etatValve2 = extraireXY(donneesValve2);
    const etatValve3 = extraireXY(donneesValve3);

      // ── Fusionner tous les timestamps en un seul axe X trié et dédupliqué ──
    const tousLesLabels = [
        ...etatFan1, ...etatFan2, ...etatPompe,
        ...etatPorte, ...etatValve1, ...etatValve2, ...etatValve3
    ]
    .map(function(point) { return point.x; })          // garder uniquement le x
    .filter(function(val, idx, arr) {                   // dédupliquer
        return arr.indexOf(val) === idx;
    })
    .sort();  
    
    return {
        g1_labels,
        g2_labels:tousLesLabels,
        tempCapteur1,
        tempCapteur2,
        tempCapteur3,
        humiditeCapteur1,
        etatFan1,
        etatFan2,
        etatPompe,
        etatPorte,
        etatValve1,
        etatValve2,
        etatValve3
    };
}


// ─────────────────────────────────────────────────────
// 2. CRÉER ET AFFICHER LES GRAPHIQUES
// ─────────────────────────────────────────────────────

// On garde une référence aux graphiques pour pouvoir les détruire
let chartTemp  = null;
let chartState = null;

async function initialiserGraphiques() {

    // On attend que les données soient prêtes
    const donnees = await chargerHistorique();

    // Si les graphiques existent déjà, on les détruit avant de recréer
    if (chartTemp  !== null) { chartTemp.destroy();  }
    if (chartState !== null) { chartState.destroy(); }

     // ── Graphique 1 : Températures + Humidité ────────
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: donnees.g1_labels,
            datasets: [
                {
                    label:       "Capteur 1 (°C)",
                    data:        donnees.tempCapteur1,
                    borderColor: "red",
                    tension:     0.3,
                    pointRadius: 2,
                    yAxisID:     'yTemp'
                },
                {
                    label:       "Capteur 2 (°C)",
                    data:        donnees.tempCapteur2,
                    borderColor: "blue",
                    tension:     0.3,
                    pointRadius: 2,
                    yAxisID:     'yTemp'
                },
                {
                    label:       "Capteur 3 (°C)",
                    data:        donnees.tempCapteur3,
                    borderColor: "green",
                    tension:     0.3,
                    pointRadius: 2,
                    yAxisID:     'yTemp'
                },
                {
                    label:            "Humidité Capteur 1 (%)",
                    data:             donnees.humiditeCapteur1,
                    borderColor:      "orange",
                    borderDash:       [6, 3],
                    tension:          0.3,
                    pointRadius:      2,
                    yAxisID:          'yHumidite'
                }
            ]
        },
        options: {
            responsive:          true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                yTemp: {
                    type:     'linear',
                    position: 'left',
                    title:    { display: true, text: "Température (°C)" }
                },
                yHumidite: {
                    type:     'linear',
                    position: 'right',
                    min:      0,
                    max:      100,
                    title:    { display: true, text: "Humidité (%)" },
                    grid:     { drawOnChartArea: false }
                },
                x: {
                    title: { display: true, text: "Heure" },
                    ticks: { maxTicksLimit: 12, maxRotation: 45 }
                }
            }
        }
    });

    new Chart(state, {
    type: 'line',
    data: {
        labels: donnees.g2_labels,
        datasets: [
            {
                label:           "Fan 1 (%)",
                data:            donnees.etatFan1,   // [{x: "12:00:01", y: 75}, ...]
                borderColor:     "#e74c3c",
                backgroundColor: "rgba(231, 76, 60, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yFan'
            },
            {
                label:           "Fan 2 (%)",
                data:            donnees.etatFan2,
                borderColor:     "#e67e22",
                backgroundColor: "rgba(230, 126, 34, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yFan'
            },
            {
                label:           "Pompe",
                data:            donnees.etatPompe,
                borderColor:     "#3498db",
                backgroundColor: "rgba(52, 152, 219, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yEtat'
            },
            {
                label:           "Porte",
                data:            donnees.etatPorte,
                borderColor:     "#2ecc71",
                backgroundColor: "rgba(46, 204, 113, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yEtat'
            },
            {
                label:           "Valve 1",
                data:            donnees.etatValve1,
                borderColor:     "#9b59b6",
                backgroundColor: "rgba(155, 89, 182, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yEtat'
            },
            {
                label:           "Valve 2",
                data:            donnees.etatValve2,
                borderColor:     "#1abc9c",
                backgroundColor: "rgba(26, 188, 156, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yEtat'
            },
            {
                label:           "Valve 3",
                data:            donnees.etatValve3,
                borderColor:     "#95a5a6",
                backgroundColor: "rgba(149, 165, 166, 0.1)",
                stepped:         'before',
                pointRadius:     0,
                borderWidth:     2,
                fill:            true,
                yAxisID:         'yEtat'
            }
        ]
    },
    options: {
        parsing:             false,   // ← indispensable pour le format {x, y}
        responsive:          true,
        maintainAspectRatio: false,
        plugins: { legend: { position: 'top' } },
        scales: {
            yEtat: {
                type:     'linear',
                position: 'left',
                min:      0,
                max:      1,
                ticks: {
                    stepSize: 1,
                    callback: function(valeur) {
                        return valeur === 1 ? 'ON' : 'OFF';
                    }
                },
                title: { display: true, text: "État" }
            },
            yFan: {
                type:     'linear',
                position: 'right',
                min:      0,
                max:      100,
                ticks: {
                    stepSize: 25,
                    callback: function(valeur) {
                        return valeur + '%';
                    }
                },
                title: { display: true, text: "Vitesse fan (%)" },
                grid:  { drawOnChartArea: false }
            },
            x: {
                type:  'category',   // ← important avec parsing: false
                title: { display: true, text: "Heure" },
                ticks: { maxTicksLimit: 12, maxRotation: 45 },
                grid:  { display: true }
            }
        }
    }
});
     
}


// Lancer au chargement, puis toutes les 5 minutes
document.addEventListener('DOMContentLoaded', function() {
    initialiserGraphiques();
    setInterval(initialiserGraphiques, 5 * 60 * 1000);
    //                                 ^^^^^^^^^^^^^
    //                                 5 min × 60 sec × 1000 ms = 300 000 ms
});