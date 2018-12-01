function drawCropping(start, end) {
  $('#new-cropping').css({
    left: Math.min(start.x, end.x), top: Math.min(start.y, end.y),
    width: Math.abs(start.x - end.x), height: Math.abs(start.y - end.y)
  })
}
function parsePos(pos) {
  items = pos.split(",")
  return {x: +items[0], y: +items[1]}
}

function cropSelection(cb) {
  function getPos(event, element) {
    return {x: event.pageX - $(element).offset().left,
      y: event.pageY - $(element).offset().top}
  }
  function strPos(pos) {
    return "" + pos.x + "," + pos.y
  }
  function draw(pos) {
    drawCropping(start, pos)
  }

  var start = undefined
  $('.photo').on({
    mousedown: function(event) {
      start = getPos(event, this)
      return false
    },
    mousemove: function(event) {
      if (start) draw(getPos(event, this))
      return false
    },
    mouseup: function(event) {
      var end = getPos(event, this)
      draw(end)
      cb(strPos(start)+"-"+strPos(end))

      start = undefined
      return false
    }
  }).append('<div id="new-cropping" class="cropping">')
}
