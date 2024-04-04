<template>
  <div>
    <div id="map"></div>
    <div id="weather-info">
      <h2>{{ selectedPlace }}</h2>
      <p>{{ weather }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedPlace: "",
      weather: "",
    };
  },
  mounted() {
    // Initialize the map
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 0, lng: 0 },
      zoom: 2,
    });

    // Add a click event listener to the map
    map.addListener("click", (event) => {
      const latLng = event.latLng;
      const lat = latLng.lat();
      const lng = latLng.lng();

      // Call the weather API to get the weather information
      // Replace 'YOUR_API_KEY' with your actual API key
      fetch(
        `https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${lat},${lng}`
      )
        .then((response) => response.json())
        .then((data) => {
          this.selectedPlace = data.location.name;
          this.weather = data.current.condition.text;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  },
};
</script>

<style>
#map {
  height: 400px;
}
</style>
