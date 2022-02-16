// Variables from discover page 
$list = $('.image_city')
$discovercard = $('#discovercard')
$contentimg = $('#contentimg')



// This function handles clicks for the list of locations and populates the div block with location data
$list.click(function(){
    let img = $(this).find('#discover_img').clone()
    console.log(img)
    let description = $(this).find('#city_description').clone()
    console.log(description)
    $discovercard.empty()
    $discovercard.append(img[0])
    $discovercard.append(description[0])
    $discovercard.children('p').toggleClass('d-none')
  
  
})