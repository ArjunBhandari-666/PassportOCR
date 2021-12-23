def full_OCR(self):
        bounded = self.img.copy()
        res = np.zeros_like(self.gray_img)

        string = image_to_string(Image.open(self.image_file))
        if string == u'':
            return bounded, res

        boxes = image_to_boxes(Image.open(self.image_file))
        boxes = [map(int, i) for i in [b.split(" ")[1:-1] for b in boxes.split("\n")]]

        for box in boxes:
            b = (int(box[0]), int(self.h - box[1]), int(box[2]), int(self.h - box[3]))
            cv2.rectangle(bounded, (b[0], b[1]), (b[2], b[3]), (0, 255, 0), 2)
            cv2.rectangle(res, (b[0], b[1]), (b[2], b[3]), 255, -1)

        return bounded, res 