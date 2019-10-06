limit = 0;
checked = 0;
$(document).ready(function () {
    document.querySelectorAll('.topping-control').forEach(function (e) {
        e.addEventListener('change', function () {
            limit = parseInt(e.value);
            checked = 0;
            removeChecks(e.dataset.control);
            if (limit == checked) {
                disableChecks(e.dataset.control);
            } else {
                enableChecks(e.dataset.control);
                makeChecksRequired(e.dataset.control);
            }
        });
    });

    addCheckboxListener('sic_toppings');
    addCheckboxListener('reg_toppings');
});

function addCheckboxListener(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        e.addEventListener('change', function () {
            if (e.checked == true) {
                checked += 1;
            } else if (e.checked == false) {
                checked -= 1;
                enableChecks(cls);
            }
            if (checked == limit) {
                disableChecks(e.name);
                makeChecksNotRequired(e.name);
            } else if (checked < limit) {
                enableChecks(e.name);
            }
        });
    });
}

function enableChecks(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        e.disabled = false;
    });
}

function makeChecksRequired(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        e.required = true;
    });
}

function makeChecksNotRequired(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        if (e.checked == false) {
            e.required = false;
        }
    });
}

function disableChecks(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        if (e.checked == false) {
            e.disabled = true;
        }
    });
}

function removeChecks(cls) {
    document.getElementsByName(cls).forEach(function (e) {
        e.checked = false;
    });
}