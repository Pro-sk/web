function checkStar(id,len)
{
    for(var i=1;i<6;i++)
    {
        $('#ch'+i).css('color','white');
    }
    $('#star').val(parseInt(len));
    var length = parseInt(len)+1;
    for(var j=1;j<length;j++)
    {
        $('#ch'+j).css('color','orange');
    }
}