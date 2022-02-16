// Variables from discover page 
$list = $('.image_city')
$discovercard = $('#discovercard')
$contentimg = $('#contentimg')



// This function handles clicks for the list of locations and populates the div block with location data
$list.click(function(){
    console.log($(this))
    //grabbing city primary key
    let primarykey = $(this).find('#locationid').clone()
    $(primarykey).attr('id', 'discovercard_pk')
    // grabs image from list and then assigns new id
    let img = $(this).find('#discover_img').clone()
    $(img).attr('id', 'discovercard_img')
    //grabs description and then assigns new id 
    let description = $(this).find('#city_description').clone()
    $(description).attr('id', 'discovercard_description')
    //grabs city name & country name and then assigns new id's 
    let city = $(this).find('#discover_city').clone()
    $(city).attr('id', 'discovercard_city')
    let country = $(this).find('#discover_country').clone()
    $(country).attr('id', 'discovercard_country')
    // populate discover card
    $discovercard.empty()
    $discovercard.append(primarykey)
    $discovercard.append(img[0])
    $discovercard.append(city[0])
    $discovercard.append(country[0])
    $discovercard.append(description[0])
    $discovercard.children('p').toggleClass('d-none')
});