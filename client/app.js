function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

   var url = "http://127.0.0.1:5000/predict_home_price1"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}


function onClickedEstimatePrice1() {
  console.log("Estimate price button clicked");
  var form=document.getElementById('form1');
 var bedrooms=form.bedrooms.value;
 var bathrooms=form.bathrooms.value;
 var sqft_lv=form.sqft_lv.value;
 var sqft_lot=form.sqft_lot.value;
 var floors= form.floors.value;
 var  condition=form.condition.value;
 var grade=form.grade.value;
 var sqft_above=form.sqft_above.value;
 var sqft_basement=form.sqft_basement.value;
 var lat=form.lat.value;
 var longg=form.longg.value;
  var estPrice = document.getElementById("uiEstimatedPrice2");
   var url = "http://127.0.0.1:5000/predict_home_price2"; 
  $.post(url, {
     bedrooms:bedrooms,
  bathrooms: bathrooms,
  sqft_lv: sqft_lv,
 sqft_lot: sqft_lot,
 floors: floors,
  condition: condition,
 grade: grade,
  sqft_above: sqft_above,
  sqft_basement: sqft_basement,
  lat: lat,
  longg: longg
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "  dollars</h2>";
      console.log(status);
  });
}
function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
 // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}



function model1Open()
{

document.getElementById('model1').style.display='block';
document.getElementById('cont').style.display='none';


}

function model2Open()
{

document.getElementById('model2').style.display='block';
document.getElementById('cont').style.display='none';


}
function openAbout()
{

document.getElementById('about').style.display='block';
document.getElementById('cont').style.display='none';


}
function openIndex()
{
document.getElementById('model1').style.display='none';
document.getElementById('about').style.display='none';
document.getElementById('model2').style.display='none';
document.getElementById('cont').style.display='block';

}


window.onload = onPageLoad;