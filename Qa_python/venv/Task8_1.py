# # ---- Task 1 ----
# class Triangle:
#     def __init__(self,
#                  angle1=int(input('1st angle: ')),
#                  angle2=int(input('2nd angle: ')),
#                  angle3=int(input('3rd angle: '))):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#         self.sum_angle = self.angle1 + self.angle2 + self.angle3
#         self.number_of_sides = 3
#
#     def check_angles(self):
#         # print(self.sum_angle)
#         if self.sum_angle == 180:
#             print(True)
#         else:
#             print(False)
#
#
# triangle_1 = Triangle()
# print('The amount of side is {}' .format(triangle_1.number_of_sides))
# triangle_1.check_angles()

# ---- Task 2 ----

class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for string in self.lyrics:
            print(string)


happy_bday = Songs(["May god bless you, ",
                    "Have a sunshine on you,",
                    "Happy Birthday to you !"])

happy_bday.sing_me_a_song()
