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
    history.pushState(null, "", url);
    url = getUrl();

    showLoading();
    $.get(url + "?inner_html=true", function (data) {
        var highestId = setInterval(function () {}, 20);
        for (var i = 0; i <= highestId; i++) {
            clearInterval(i);
        }
        
            setTimeout(function () {
                $(".container-content").html(data);
                hideLoading();
                setComponents();
            }, 200);
            
        }).fail(function () {
            setTimeout(function () {
                $(".container-content").html(
                    "<h1 class='text-color-default m-5'>Erro 404!<br>Página não encontrada</h1>"
                );
                hideLoading();
                setComponents();
            }, 200);
        });
}

function setComponents() {
    $(".redirect-component").off("click");
    $(".redirect-component").click(function () {
        loadContent($(this).attr("data-url"));
    });

    $(".form-component").off("submit");
    $(".form-component").on("submit", function (event) {
        event.preventDefault();

        showLoading();
    
        var formData = new FormData(this);
    
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: formData,
            processData: false, // Impede que jQuery processe os dados
            contentType: false, // Impede que jQuery defina o cabeçalho Content-Type
            success: function (data) {
                setTimeout(function () {
                    $(".container-content").html(data);
                    $(".form-component")[0].reset();
                    hideLoading();
                    setComponents();
                }, 200);
            },
            error: function (data) {
                setTimeout(function () {
                    $(".container-content").html(data);
                    hideLoading();
                    setComponents();
                }, 200);
            },
        });
    });
}

function getUrl() {
    return window.location.href.split("#")[0].replace("inner_html=true", "");
}
function showLoading() {
    $("#loading").addClass("show");
}

function hideLoading() {
    setTimeout(function () {
        $("#loading").removeClass("show");
    }, 100);
}
