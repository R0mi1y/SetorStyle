let previousUrl = window.location.href.replace("#", "");

window.addEventListener("popstate", function (event) {
    console.log("popstate", event);
    if (previousUrl !== getUrl()) {
        loadContent(window.location.href);
        previousUrl = getUrl();
    }
});

$(document).ready(function () {
    loadContent(getUrl());
});

function loadContent(url) {
    history.pushState(null, '', url);
    url = getUrl();
    
    showLoading();
    setTimeout(function () {
        $.get(url + "?inner_html=true", function (data) {
            $(".container-content").html(data);
            hideLoading();
        }).fail(function () {
            $(".container-content").html(
                "<h1 class='text-color-default m-5'>Erro 404!<br>Página não encontrada</h1>"
            );
            hideLoading();
        });
    }, 200);
}

function getUrl() {
    return window.location.href.split("#")[0];
}

function showLoading() {
    $("#loading").addClass("show");
}

function hideLoading() {
    setTimeout(function () {
        $("#loading").removeClass("show");
    }, 100);
}