{ List.map
  =
    \(_ : Type) ->
    \(_ : Type) ->
    \(_ : _@1 -> _@1) ->
    \(_ : List _@2) ->
      List/fold
        _@3
        _
        (List _@2)
        (\(_ : _@3) -> \(_ : List _@3) -> [ _@3 _@1 ] # _)
        ([] : List _@2)
, Text.concatSep
  =
    \(_ : Text) ->
    \(_ : List Text) ->
      merge
        { Empty = "", NonEmpty = \(_ : Text) -> _ }
        ( List/fold
            Text
            _
            < Empty | NonEmpty : Text >
            ( \(_ : Text) ->
              \(_ : < Empty | NonEmpty : Text >) ->
                merge
                  { Empty = < Empty | NonEmpty : Text >.NonEmpty _@1
                  , NonEmpty =
                      \(_ : Text) ->
                        < Empty | NonEmpty : Text >.NonEmpty "${_@2}${_@4}${_}"
                  }
                  _
            )
            < Empty | NonEmpty : Text >.Empty
        )
}
