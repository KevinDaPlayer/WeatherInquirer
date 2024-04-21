<template>
  <div>
    <div id="map" style="height: 400px"></div>
    <div>
      <h2>Weather</h2>
      <p>Temperature: {{ weather.temp }}</p>
      <p>Feels Like: {{ weather.feels_like }}</p>
      <p>Min Temperature: {{ weather.temp_min }}</p>
      <p>Max Temperature: {{ weather.temp_max }}</p>
      <p>Weather: {{ weather.weather }}</p>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import L from "leaflet";

export default {
  name: "LealeftMap",
  data() {
    return {
      map: null,
      lat: 0,
      lon: 0,
      weather: {
        temp: 0,
        feels_like: 0,
        temp_min: 0,
        temp_max: 0,
        weather: "",
      },
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      this.map = L.map("map").setView([51.505, -0.09], 13);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
      }).addTo(this.map);
      this.map.on("click", this.onMapClick);
    },
    onMapClick(e) {
      const { lat, lng } = e.latlng;
      this.lat = lat;
      this.lon = lng;
      this.fetchWeather();
    },
    fetchWeather() {
      const url = `http://localhost:5000/weather?lat=${this.lat}&lon=${this.lon}`;
      axios.get(url).then((response) => {
        console.log(response.data);
        const data = response.data;
        this.weather = {
          temp: data.main.temp,
          feels_like: data.main.feels_like,
          temp_min: data.main.temp_min,
          temp_max: data.main.temp_max,
          weather: data.weather[0].main,
        };
      });
    },
  },
};
</script>
<style>
@import "~leaflet/dist/leaflet.css";
</style>
