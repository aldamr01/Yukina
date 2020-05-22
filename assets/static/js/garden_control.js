var interval = 1000;  // 1000 = 1 second, 3000 = 3 seconds
function doAjax() {
    $.ajax({
            type: 'GET',
            url: '/api/v1/sensorcontrol/',
            data: $(this).serialize(),
            dataType: 'json',
            success: function (data) {
                    // $('#hidden').val(data);// first set the value
                    if(data['status'] == true){
                        document.getElementById("status_i").className = "btn btn-success";
                        document.getElementById("status_i").innerHTML = "active";
                    }else{                        
                        document.getElementById("status_i").className = "btn btn-default";
                        document.getElementById("status_i").innerHTML = "inactive";
                    }

                    if(data['pump_nutrient_a'] == true){
                        document.getElementById("pump_nutrient_a").className = "btn btn-success";
                        document.getElementById("pump_nutrient_a").innerHTML = "working";
                    }else{
                        document.getElementById("pump_nutrient_a").className = "btn btn-default";
                        document.getElementById("pump_nutrient_a").innerHTML = "iddle";
                    }

                    if(data['pump_nutrient_b'] == true){
                        document.getElementById("pump_nutrient_b").className = "btn btn-success";
                        document.getElementById("pump_nutrient_b").innerHTML = "working";
                    }else{
                        document.getElementById("pump_nutrient_b").className = "btn btn-default";
                        document.getElementById("pump_nutrient_b").innerHTML = "iddle";
                    }

                    if(data['pump_water'] == true){
                        document.getElementById("pump_water").className = "btn btn-success";
                        document.getElementById("pump_water").innerHTML = "working";
                    }else{
                        document.getElementById("pump_water").className = "btn btn-default";
                        document.getElementById("pump_water").innerHTML = "iddle";
                    }
            },
            complete: function (data) {
                    // Schedule the next
                    setTimeout(doAjax, interval);
            }
    });
}
setTimeout(doAjax, interval);