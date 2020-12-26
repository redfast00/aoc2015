import Data.List

main = do
    iput <- lines <$> readFile "input"
    let parsed = map parse iput
    print $ sum $ map needed parsed
    print $ sum $ map ribbon parsed

data Wrapping = Wrap Int Int Int

parse :: String -> Wrapping
parse line = case ints of
    [a,b,c] -> Wrap a b c
    _       -> error "error parsing"
    where ints = map read $ words [if c == 'x' then ' ' else c | c <- line]

needed :: Wrapping -> Int
needed (Wrap l w h) = 2*l*w + 2*w*h + 2*h*l + extraWrapping
    where extraWrapping = minimum [l*w, w*h, h*l]

ribbon :: Wrapping -> Int
ribbon (Wrap l w h) = 2 * f +  2 * s + bowtie
    where bowtie = l * w * h
          [f, s] = drop 1 $ sortBy (flip compare) [l, w, h]
