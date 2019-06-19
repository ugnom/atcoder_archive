
-- Multi lines of lists
import Data.Traversable
import Data.List
import Control.Monad
import Data.Maybe

main = do
  (t:a:b:c:xs) <- map read . words <$> getLine
  ps <- for [1..t] $ \x -> do
    read <$> getLine
  putStrLn . show $ solve ps (a,b,c)

solve :: [Int] -> (Int,Int,Int) -> Int
solve ps (a,b,c) =
  let cands = replicateM (length ps) ['a','b','c','n']
  in minimum . catMaybes $ map (calcOne ps (a,b,c)) cands


calcOne ps (a,b,c) s =
  if 'a' `elem` s &&  'b' `elem` s && 'c' `elem` s then
    let ((va,ca),(vb,cb),(vc,cc)) = calc ps (a,b,c) s
    in Just   ((ca + (abs (a - va)))
         + (cb + (abs (b - vb)))
         + (cc + (abs (c - vc))) - 30)
  else
    Nothing

calc [] (a,b,c) [] = ((0,0),(0,0),(0,0))
calc (p:ps) (a,b,c) (s:ss) =
  let ((va,ca),(vb,cb),(vc,cc)) = calc ps (a,b,c) ss
  in case s of
    'a' -> ((va+p,ca+10),(vb,cb),(vc,cc))
    'b' -> ((va,ca),(vb+p,cb+10),(vc,cc))
    'c' -> ((va,ca),(vb,cb),(vc+p,cc+10))
    'n' -> ((va,ca),(vb,cb),(vc,cc))
