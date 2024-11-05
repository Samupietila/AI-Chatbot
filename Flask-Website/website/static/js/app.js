$(document).ready(function () {
  $("#chat-widget-button").on("click", function () {
    $("#chat-widget").toggleClass("d-none");
  });

  $("#chat-widget-close-button").on("click", function () {
    $("#chat-widget").addClass("d-none");
  });

  $("#chat-widget-input").keypress(function (e) {
    if (e.which == 13) {
      sendMessage($("#chat-widget-input").val());
      $("#chat-widget-input").val("");
    }
  });

  $("#button-container").on("click", ".btn-secondary", function () {
    const userMessage = $(this).data("payload");
    console.log("User message: ", userMessage);
    sendMessage(userMessage, $(this).text());
  });

  function clearButtons() {
    $("#button-container").empty();
  }

  $("#chat-widget-send-button").on("click", function () {
    sendMessage($("#chat-widget-input").val());
    $("#chat-widget-input").val("");
  });

  function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    for (let i = 0; i < cookieArr.length; i++) {
      let cookiePair = cookieArr[i].split("=");
      if (name == cookiePair[0].trim()) {
        return decodeURIComponent(cookiePair[1]);
      }
    }
    return null;
  }

  function sendMessage(userMessage, buttonName) {
    if (userMessage) {
      clearButtons();
      let language = getCookie("language");
      let data = {
        message: userMessage,
        user_id: "under work",
        metadata: {
          language: language,
        },
      };
      console.log(data);
      if (buttonName) {
        var messageHtml =
          '<div class=chat-widget-message-sender><div class="inner-message id="user-message"><strong>You:</strong><div class="chat-widget-message chat-widget-message-right">' +
          "<mark>Button pressed:</mark> " +
          buttonName +
          "</div></div></div>";
      } else {
        var messageHtml =
          '<div class=chat-widget-message-sender><div class="inner-message id="user-message"><strong>You:</strong><div class="chat-widget-message chat-widget-message-right">' +
          userMessage +
          "</div></div></div>";
      }
      $("#chat-widget-messages").append(messageHtml);
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/webhook",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (data) {
          var botResponse = data.message;
          var buttons = data.buttons;
          var botMessageHtml =
            '<div class=chat-widget-message-bot><div class="inner-message"><strong>Essi-Bot:</strong><div class="chat-widget-message chat-widget-message-left">' +
            botResponse +
            "</div></div></div>";
          $("#chat-widget-messages").append(botMessageHtml);
          if (buttons.length > 0) {
            const buttonHtml = $('<div class="button-container mt-2"></div>');
            buttons.forEach(function (button) {
              const buttonElement = $(
                '<button class="btn btn-secondary mt-1"></button>'
              )
                .text(button.title)
                .data("payload", button.payload);
              buttonHtml.append(buttonElement);
            });
            $("#button-container").append(buttonHtml);
          }
        },
        error: function (xhr, status, error) {
          console.error("Error status:", status);
          console.error("Error details:", error);
          console.log("Response Text: ", xhr.responseText);
        },
      });
    }
  }
});
