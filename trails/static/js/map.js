document.addEventListener("DOMContentLoaded", function () {
  // Only run the map if the #map div exists
  if (document.getElementById("map")) {
    mapboxgl.accessToken =
      "pk.eyJ1IjoibWF6MDA3IiwiYSI6ImNtOXNkbHJtZTAxangybHFwNG1va2lwNzEifQ.5bRrcTCttUXa-ULvcSSNjw";

    const map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/outdoors-v12",
      center: [6.85, 46.5], // Swiss Romande center
      zoom: 8.5,
    });

    map.addControl(new mapboxgl.NavigationControl());

    // Boot icon factory
    function createBootIcon() {
      const icon = document.createElement("img");
      icon.src = "/static/img/hike_boot.png";
      icon.style.width = "40px";
      icon.style.height = "40px";
      return icon;
    }

    // Markers for each trail
    const markers = {
      CreuxDuVar: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.7289, 46.9296])
        .setPopup(new mapboxgl.Popup().setText("Creux du Van"))
        .addTo(map),

      DentDeJaman: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.9613, 46.4401])
        .setPopup(new mapboxgl.Popup().setText("Dent de Jaman"))
        .addTo(map),

      Grammont: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.8627, 46.3214])
        .setPopup(new mapboxgl.Popup().setText("Le Grammont"))
        .addTo(map),

      LacDeTaney: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.8986, 46.2939])
        .setPopup(new mapboxgl.Popup().setText("Lac de Taney"))
        .addTo(map),

      LesPleiades: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.9321, 46.4848])
        .setPopup(new mapboxgl.Popup().setText("Les Pléiades"))
        .addTo(map),

      LaTineDeConflens: new mapboxgl.Marker({ element: createBootIcon() })
        .setLngLat([6.7125, 46.613])
        .setPopup(new mapboxgl.Popup().setText("La Tine de Conflens"))
        .addTo(map),
    };

    setTimeout(() => {
      map.resize();
    }, 400);
  }
});
