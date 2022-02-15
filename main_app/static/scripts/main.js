// Variables from discover page 
$list = $('.city_list')
$discovercard = $('#discovercard')


// This function handles clicks for the list of locations and populates the div block with location data
$list.click(function(){
    let description = $(this).find('#city_description').html()
    $discovercard.empty()
    $discovercard.append(description)
})