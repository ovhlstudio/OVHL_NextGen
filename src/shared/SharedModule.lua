local Shared = {}

function Shared.Greet(name)
    return "Welcome to OVHL_NextGen, " .. (name or "User") .. "!"
end

return Shared
