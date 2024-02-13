#!/usr/bin/node
// Define Rectangle Class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let r = '';
        for (let j = 0; j < this.width; j++) {
          r += 'X';
        }
        console.log(r);
      }
    }
  }
}
module.exports = Rectangle;
