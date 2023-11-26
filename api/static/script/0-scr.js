document.addEventListener('keydown', function (event) {
  // Check if the pressed key is Enter (key code 13)
  city = document.getElementById('city-input')
  if (event.key === 'Enter') {
    console.log(city.value);
    // Redirect to the specified URL
    window.location.href = `https://www.dehao.tech/weather/${city.value}`;
  }
});
