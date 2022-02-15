$locations = $('.location');
$locationContent = $('.locationContent')
console.log($locations)

$locationContent.click(function() {
    $(this).toggleClass('d-none')
})

$locations.click(function(){
    console.log('this is a click!')
    console.log($(this).children().toggleClass('d-none'))
})