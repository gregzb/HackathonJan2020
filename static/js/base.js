jQuery(function($) {
  $('.draggablelist').each((idx, el) => {
    let panelList = $(el);
    panelList.sortable({
        // Only make the .panel-heading child elements support dragging.
        // Omit this to make then entire <li>...</li> draggable.
        handle: '.drag-el',
        update: function() {
            $('.item', panelList).each(function(index, elem) {
                var $listItem = $(elem),
                    newIndex = $listItem.index();
                    // Persist the new indices.
            });
        }
    });
  });

  $('.title-input').each((idx, el) => {
    el.addEventListener('focusout', (e) => {
      console.log("Title was set");
      console.log(e);
    });
  });

  let handle_focus_out = (el, e) => {
    let parent = e.target.parentElement.parentElement.parentElement.parentElement.parentElement;

    let anyEmpty = false;

    console.log("childreN!");
    console.log(parent);

    $(parent).children().each((idx, item) => {
      console.log("thingy: ");
      console.log(item);
      let input_param = $(item).children()[0];
      //input_param = $(input_param).children()[0];
      input_param = $(input_param).children()[1];
      input_param = $(input_param).children()[0];
      input_param = $(input_param).children()[0];
      let text = $(input_param).val();
      console.log(text);
      if ( text.length == 0) {
        anyEmpty = true;
      }
    });

    if (anyEmpty == false) {
      console.log("parent: ~~~~~~");
      console.log(parent);
      let new_one = $(e.target.parentElement.parentElement.parentElement.parentElement).clone(false);
      new_one[0].addEventListener('focusout', (e) => {
        handle_focus_out(el, e);
      });
      let child = $(new_one).children()[0];
      child = $(child).children()[1];
      child = $(child).children()[0];
      child = $(child).children()[0];
      $(child).val("");
      $(parent).append(new_one);
    }
  };

  $('.todo-input').each((idx, el) => {
    el.addEventListener('focusout', (e) => {
      handle_focus_out(el, e);
      // let parent = e.target.parentElement.parentElement.parentElement.parentElement.parentElement;
      //
      // let anyEmpty = false;
      //
      // $(parent).each((idx, item) => {
      //   let input_param = $(item).children()[0];
      //   input_param = $(input_param).children()[0];
      //   input_param = $(input_param).children()[1];
      //   input_param = $(input_param).children()[0];
      //   input_param = $(input_param).children()[0];
      //   let text = $(input_param).val();
      //   if ( text.length == 0) {
      //     anyEmpty = true;
      //   }
      // });
      //
      // if (anyEmpty == false) {
      //   let new_one = $(e.target.parentElement.parentElement.parentElement.parentElement).clone();
      //   let child = $(new_one).children()[0];
      //   child = $(child).children()[1];
      //   child = $(child).children()[0];
      //   child = $(child).children()[0];
      //   $(child).val("");
      //   $(parent).append(new_one);
      // }

    });
  });
});
