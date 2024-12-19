import System.IO
import Data.Char


split :: Eq a => a -> [a] -> [[a]]
split d [] = []
split d s = x : split d (drop 1 y) where (x,y) = span (/= d) s

fwdiff:: [Int] -> [Int]
fwdiff [] = []
fwdiff [a] = []
fwdiff (a:b:xs) = (a - b) : fwdiff (b:xs)

conditionWithin1and3:: [Int] -> Bool
conditionWithin1and3 = foldr (\ a -> (&&) (a >= 1 && a <= 3 || a <= - 1 && a >= - 3)) True

conditionAllIncreaseOrDecrease:: [Int] -> Bool
conditionAllIncreaseOrDecrease xs =  all ( > 0) xs || all ( < 0) xs

conditions:: [Int] -> Bool
conditions xs = conditionWithin1and3 xs && conditionAllIncreaseOrDecrease xs

bool2int:: Bool -> Int
bool2int True = 1
bool2int False = 0

main::IO()
main = do
    file <- openFile "input.txt" ReadMode
    contents <- hGetContents file

    let s = split '\n' contents :: [String]
    let c = map (split ' ') s

    let b = map (map (\x -> read x :: Int) ) c
    print $ sum (map (bool2int.conditions.fwdiff) b)
    
    hClose file
    