fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(response => response.json())
.then(data => {
    $('#hello').append(data.hello);
})