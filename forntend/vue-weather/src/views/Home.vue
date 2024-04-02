import { search } from "core-js/fn/symbol"

<template>
  <div>
    <input type="text" v-model="searchQuery" placeholder="請輸入您的城市" />
    <button @click="searchWeather">Search</button>

    <table>
      <thead>
        <tr>
          <th>Location</th>
          <th>Temperature</th>
          <th>Weather</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="result in searchResults" :key="result.id">
          <td>{{ result.location }}</td>
          <td>{{ result.temperature }}</td>
          <td>{{ result.weather }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchQuery: "",
      searchResults: [],
    };
  },
  methods: {
    searchWeather() {
      axios
        .get(`http://localhost:3000/weather?city=${this.searchQuery}`)
        .then((response) => {
          const data = response.data;
          if (data.cod === "200") {
            const result = {
              location: data.name,
              temperature: data.main.temp,
              weather: data.weather[0].description,
              id: data.id,
            };
          } else {
            const result = {
              location: "Not Found",
              temperature: "Not Found",
              weather: "Not Found",
            };
          }
        });
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
