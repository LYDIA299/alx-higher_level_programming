#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      let c = '';
      for (let j = this.width; j > 0; j--) {
        c = c + 'X';
      }
      console.log(c);
    }
  }
}
module.exports = Rectangle;
