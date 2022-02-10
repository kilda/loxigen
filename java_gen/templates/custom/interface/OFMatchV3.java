
    /**
     * Returns a value for the given field if:
     * <ul>
     * <li>Field is supported
     * <li>Field is not fully wildcarded
     * </ul>
     * If one of the above conditions does not hold, returns null. Value is returned masked if partially wildcarded.
     *
     * @param <F> MatchField type
     * @param field Match field to retrieve
     * @return Value of match field (may be masked), or <code>null</code> if field is one of the conditions above does not hold.
     * @throws UnsupportedOperationException If field is not supported.
     */
    public <F extends OFValueType<F>> F getWithoutPrerequisitesCheck(MatchField<F> field)
            throws UnsupportedOperationException;

    /**
     * Returns the masked value for the given field from this match, along with the mask itself.
     *
     * @param <F> MatchField type
     * @param field Match field to retrieve.
     * @return Masked value of match field or null if no mask is set.
     * @throws UnsupportedOperationException If field is not supported.
     */
    public <F extends OFValueType<F>> Masked<F> getMaskedWithoutPrerequisitesCheck(MatchField<F> field)
            throws UnsupportedOperationException;

    /**
     * Get an Iterable over the match fields that have been specified for the
     * match. This includes the match fields that are exact or masked match
     * (but not fully wildcarded).
     *
     * @return the Iterable of MatchField
     */
    public Iterable<MatchField<?>> getMatchFieldsWithoutPrerequisitesCheck();
