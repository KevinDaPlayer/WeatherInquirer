import { search } from "core-js/fn/symbol"

<template>
  <div>
    <h1>Weather Searching</h1>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/map">Leaflet</router-link>
    </nav>
    <input type="text" v-model="searchQuery" placeholder="請輸入您的城市" />
    <button @click="searchWeather">Search</button>

    <table>
      <thead>
        <tr>
          <th>位置</th>
          <th>溫度</th>
          <th>天氣</th>
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
        .get(`http://localhost:5000/weather?city=${this.searchQuery}`)
        .then((response) => {
          const data = response.data;
          let result;
          if (data.cod === "200" || data.cod === 200) {
            result = {
              location: data.name,
              temperature: data.main.temp,
              weather: data.weather[0].description,
              id: data.id,
            };
          } else {
            result = {
              location: "Not Found",
              temperature: "Not Found",
              weather: "Not Found",
            };
          }
          this.searchResults = [result];
        });
    },
  },
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #f5f5f5;
}
button {
  padding: 10px 20px;
  background-color: #ad783c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #788078;
}

input[type="text"] {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type="text"]:focus {
  outline: none;
  border-color: #ad783c;
}
</style>
