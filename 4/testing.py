import unittest

from solution import *


class TestSolution(unittest.TestCase):
    def assertValid(self, field):
        def inner(x):
            self.assertTrue(validators[field](x))

        return inner

    def assertInvalid(self, field):
        def inner(x):
            self.assertFalse(validators[field](x))

        return inner

    def test_byr(self):
        self.assertValid('byr')('2002')
        self.assertInvalid('byr')('2003')

    def test_hgt(self):
        self.assertValid('hgt')('60in')
        self.assertValid('hgt')('190cm')
        self.assertInvalid('hgt')('190in')
        self.assertInvalid('hgt')('190')

    def test_hcl(self):
        self.assertValid('hcl')('#123abc')
        self.assertInvalid('hcl')('#123abz')
        self.assertInvalid('hcl')('123abc')

    def test_ecl(self):
        self.assertValid('ecl')('brn')
        self.assertInvalid('ecl')('brnbrn')
        self.assertInvalid('ecl')('wat')
        self.assertInvalid('ecl')('brn2')

    def test_pid(self):
        self.assertValid('pid')('000000001')
        self.assertInvalid('pid')('0123456789')
        self.assertInvalid('pid')('12345678')

    def test_invalid(self):
        self.assertFalse(validate('eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'))
        self.assertFalse(validate('iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946'))
        self.assertFalse(validate('hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277'))
        self.assertFalse(validate('hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'))
    
    def test_valid(self):
        self.assertTrue(validate('pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'))
        self.assertTrue(validate('eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm'))
        self.assertTrue(validate('hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022'))
        self.assertTrue(validate('iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'))


if __name__ == '__main__':
    unittest.main()
