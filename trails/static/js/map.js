document.addEventListener("DOMContentLoaded", function () {
  // Only run the map if the #map div exists
  if (document.getElementById("map")) {
    mapboxgl.accessToken =
      "pk.eyJ1IjoibWF6MDA3IiwiYSI6ImNtOXNkbHJtZTAxangybHFwNG1va2lwNzEifQ.5bRrcTCttUXa-ULvcSSNjw";

    const map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/outdoors-v12",
      center: [6.85, 46.5], // Swiss Romande center
      zoom: 9,
    });

    map.addControl(new mapboxgl.NavigationControl());

    // Marker 1: Rochers-de-Naye
    const boot1 = document.createElement("img");
    boot1.src = "/static/img/hike_boot.png";
    boot1.style.width = "40px";
    boot1.style.height = "40px";

    const markers = {
      rocher: new mapboxgl.Marker({ element: boot1 })
        .setLngLat([6.9795, 46.4296])
        .setPopup(new mapboxgl.Popup().setText("Rochers-de-Naye"))
        .addTo(map),

      lavaux: new mapboxgl.Marker({ element: boot2 })
        .setLngLat([6.7274, 46.4916])
        .setPopup(new mapboxgl.Popup().setText("Lavaux Vineyards"))
        .addTo(map),

      // ...and so on!
    };

    // Marker 2: Lavaux
    const boot2 = document.createElement("img");
    boot2.src = "/static/img/hike_boot.png";
    boot2.style.width = "40px";
    boot2.style.height = "40px";

    const marker2 = new mapboxgl.Marker({ element: boot2 })
      .setLngLat([6.7274, 46.4916])
      .setPopup(new mapboxgl.Popup().setText("Lavaux Vineyards"))
      .addTo(map);

    // Marker 3: Creux du Van
    const boot3 = document.createElement("img");
    boot3.src = "/static/img/hike_boot.png";
    boot3.style.width = "40px";
    boot3.style.height = "40px";

    const marker3 = new mapboxgl.Marker({ element: boot3 })
      .setLngLat([6.7289, 46.9296])
      .setPopup(new mapboxgl.Popup().setText("Creux du Van"))
      .addTo(map);

    // Connect cards to map markers
    document.querySelectorAll(".trail-card").forEach((card) => {
      card.addEventListener("click", () => {
        const trailId = card.dataset.trail; // e.g. "rocher"
        const marker = markers[trailId];

        if (marker) {
          map.flyTo({
            center: marker.getLngLat(),
            zoom: 12,
            speed: 1.2,
            curve: 1,
          });

          marker.togglePopup(); // show popup when zoomed in
        }
      });
    });
  }
});
