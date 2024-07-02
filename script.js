const weather = document.getElementById("img-weather");
const messageList = document.getElementById("message");
const temperature = document.getElementById("temperature");
const tempMode = document.getElementById("temp-mode");
const date = document.getElementById("date");
const cardColor = document.getElementById("weather-card");
const headerBg = document.getElementById("proj-header");

function getRandomWeather() {
  const weathers = ["cloudy", "sunny", "rainy"];
  const randomIndex = Math.floor(Math.random() * weathers.length);
  return weathers[randomIndex];
}

formatDate();

function formatDate() {
  const day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  const month = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];

  const dateNow = new Date();
  const dayOfWeek = day[dateNow.getDay()];
  const dateOfWeek = String(dateNow.getDate());
  const monthNow = month[dateNow.getMonth()];

  date.innerHTML = `${dayOfWeek}, ${dateOfWeek} ${monthNow}`;
}

function temp() {
  // insert logic for changing temperature and its description
  temperature.innerHTML = "35°C";
  tempMode.innerHTML = "Sunny"; 
}

function weatherVisual() {
  const weatherCondition = getRandomWeather();

  switch (weatherCondition) {
    case "cloudy":
      weather.src = "./assets/cloudy.png";
      messageList.innerHTML = "";
      messageList.innerHTML = `
        <li>Keep your pet comfortable indoors with cozy bedding and toys.</li>
        <li>Take short walks with your pet and avoid prolonged exposure to damp weather.</li>
        <li>Monitor your pet's behavior for signs of anxiety during cloudy periods.</li>`;
      headerBg.style.backgroundColor = "#def3f6ff";
      cardColor.style.background =
        "linear-gradient(121deg, #f6f6f6 31.21%, #def3f6ff 167.04%)";
      break;
    case "sunny":
      weather.src = "./assets/sunny.png";
      messageList.innerHTML = "";
      messageList.innerHTML = `
        <li>Hydrate your pet with fresh water, limit midday walks, and provide shade for cool naps.</li>
        <li>Cool down your pet with damp towels, early walks, and kiddie pools for a refreshing dip.</li>
        <li>Fresh water, shady spots, and paw protection are your pet's summer essentials!</li>`;
      headerBg.style.backgroundColor = '#fcffd6';
      cardColor.style.background =
        "linear-gradient(121deg, #f6f6f6 31.21%, #fcc949 167.04%)";

      break;
    case "rainy":
      weather.src = "./assets/rainy.png";
      messageList.innerHTML = "";
      messageList.innerHTML = `
        <li>Hydrate your pet with fresh water, limit midday walks, and provide shade for cool naps.</li>
        <li>Cool down your pet with damp towels, early walks, and kiddie pools for a refreshing dip.</li>
        <li>Fresh water, shady spots, and paw protection are your pet's summer essentials!</li>`;
      headerBg.style.backgroundColor = '#71bce4ff';
      cardColor.style.background =
        "linear-gradient(121deg, #f6f6f6 31.21%, #71bce4ff 167.04%)";
      break;
  }
}

weatherVisual();
