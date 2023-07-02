document.addEventListener('DOMContentLoaded', disableAddPassengerBtn);
document.getElementById("add_passenger").addEventListener("click", addPassenger);
document.getElementById("remove_passenger").addEventListener("click", removePassenger);

let passengers = document.getElementById("tour_quantity");

passenger_quantity = 1

function disableAddPassengerBtn() {
    let passengers = document.getElementById("tour_quantity").value;
    let slotsLeft = document.getElementById("slots_left").innerHTML;

    if (parseInt(passengers, 10) >= parseInt(slotsLeft, 10)) {
        document.getElementById('add_passenger').disabled = true;
    } else {
        document.getElementById('add_passenger').disabled = false;
    }
}
// Add a passenger to the tour detail

function addPassenger() {
    passenger_quantity += 1
    passengers.value = `${passenger_quantity}`;
    updatePrice();
    disableAddPassengerBtn();
}

// Remove a passenger from the tour detail
function removePassenger() {
    passenger_quantity -= 1
    removePassenger = document.getElementById('remove_passenger');
    addToBagBtn = document.getElementById('add_to_bag_btn');

    passengers.value = `${passenger_quantity}`;
    updatePrice();
    disableAddPassengerBtn();

    if (passenger_quantity == 0) {
        removePassenger.disabled = true;
        addToBagBtn.disabled = true;
    }
}

// Change product price depending on number of passengers
function updatePrice() {
    let tour_price = document.getElementById("tour_price").innerText;
    let price = document.getElementById("added_price");
    addToBagBtn = document.getElementById('add_to_bag_btn');


    let total_price = passenger_quantity * tour_price;
    price.innerHTML = parseFloat(total_price).toFixed(2);
    removePassenger.disabled = false;
    addToBagBtn.disabled = false;
}
