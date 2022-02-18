// Variables from discover page 
$list = $('.image_city')
$discovercard = $('#discovercard')
$discoverpostfield = $('#discover_post_container')
$contentimg = $('#contentimg')
$postbtn = $("#postbtn")



// This function handles clicks for the list of locations and populates the div block with location data
$list.click(function(){
    let post_data = $(this).find('.location_post').clone()
    $(post_data).toggleClass('d-none')
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
    $discoverpostfield.empty()
    $discovercard.append(primarykey)
    $discovercard.append(img[0])
    $discovercard.append(city[0])
    $discovercard.append(country[0])
    $discovercard.append(description[0])
    $discoverpostfield.append(post_data)
    if($($discoverpostfield).hasClass('d-none')){
        $discoverpostfield.toggleClass('d-none')
    }
    if($($postbtn).hasClass('d-none')){
        $postbtn.toggleClass('d-none')
    }
    $discovercard.children('p').toggleClass('d-none')
});