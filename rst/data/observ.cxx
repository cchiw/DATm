/*---------- begin cxx-head.in ----------*/
/*! \file observ.cxx
 *
 * Generated from observ.diderot.
 *
 * Command: /Users/chariseechiw/diderot/Diderot-Dev/bin/diderotc --exec --double observ.diderot
 * Version: vis15:2016-07-29
 */
/*---------- end cxx-head.in ----------*/

#define DIDEROT_STRAND_HAS_CONSTR
#define DIDEROT_NO_INPUTS
#define DIDEROT_STRAND_ARRAY
/*---------- begin exec-incl.in ----------*/
#define DIDEROT_STANDALONE_EXEC
#define DIDEROT_DOUBLE_PRECISION
#define DIDEROT_INT
#define DIDEROT_TARGET_SEQUENTIAL
#include "diderot/diderot.hxx"

#ifdef DIDEROT_ENABLE_LOGGING
#define IF_LOGGING(...)         __VA_ARGS__
#else
#define IF_LOGGING(...)
#endif
/*---------- end exec-incl.in ----------*/

// ***** Begin synthesized types *****

namespace Diderot {
    typedef double vec4 __attribute__ ((vector_size (32)));
    typedef double vec6 __attribute__ ((vector_size (64)));
    typedef double vec3 __attribute__ ((vector_size (32)));
    struct tensor_ref_4 : public diderot::tensor_ref<double,4> {
        tensor_ref_4 (const double *src);
        tensor_ref_4 (struct tensor_4 const & ten);
        tensor_ref_4 (tensor_ref_4 const & ten);
    };
    struct tensor_ref_3 : public diderot::tensor_ref<double,3> {
        tensor_ref_3 (const double *src);
        tensor_ref_3 (struct tensor_3 const & ten);
        tensor_ref_3 (tensor_ref_3 const & ten);
    };
    struct tensor_ref_2 : public diderot::tensor_ref<double,2> {
        tensor_ref_2 (const double *src);
        tensor_ref_2 (struct tensor_2 const & ten);
        tensor_ref_2 (tensor_ref_2 const & ten);
    };
    struct tensor_ref_2_2 : public diderot::tensor_ref<double,4> {
        tensor_ref_2_2 (const double *src);
        tensor_ref_2_2 (struct tensor_2_2 const & ten);
        tensor_ref_2_2 (tensor_ref_2_2 const & ten);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_ref_3_3 : public diderot::tensor_ref<double,9> {
        tensor_ref_3_3 (const double *src);
        tensor_ref_3_3 (struct tensor_3_3 const & ten);
        tensor_ref_3_3 (tensor_ref_3_3 const & ten);
        tensor_ref_3 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_ref_2_2_4 : public diderot::tensor_ref<double,16> {
        tensor_ref_2_2_4 (const double *src);
        tensor_ref_2_2_4 (struct tensor_2_2_4 const & ten);
        tensor_ref_2_2_4 (tensor_ref_2_2_4 const & ten);
        tensor_ref_4 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_4 : public diderot::tensor<double,4> {
        tensor_4 ()
            : diderot::tensor<double,4>()
        { }
        tensor_4 (std::initializer_list< double > const & il)
            : diderot::tensor<double,4>(il)
        { }
        tensor_4 (const double *src)
            : diderot::tensor<double,4>(src)
        { }
        tensor_4 (tensor_4 const & ten)
            : diderot::tensor<double,4>(ten._data)
        { }
        ~tensor_4 () { }
        tensor_4 & operator= (tensor_4 const & src);
        tensor_4 & operator= (tensor_ref_4 const & src);
        tensor_4 & operator= (std::initializer_list< double > const & il);
        tensor_4 & operator= (const double *src);
    };
    struct tensor_2 : public diderot::tensor<double,2> {
        tensor_2 ()
            : diderot::tensor<double,2>()
        { }
        tensor_2 (std::initializer_list< double > const & il)
            : diderot::tensor<double,2>(il)
        { }
        tensor_2 (const double *src)
            : diderot::tensor<double,2>(src)
        { }
        tensor_2 (tensor_2 const & ten)
            : diderot::tensor<double,2>(ten._data)
        { }
        ~tensor_2 () { }
        tensor_2 & operator= (tensor_2 const & src);
        tensor_2 & operator= (tensor_ref_2 const & src);
        tensor_2 & operator= (std::initializer_list< double > const & il);
        tensor_2 & operator= (const double *src);
    };
    struct tensor_3 : public diderot::tensor<double,3> {
        tensor_3 ()
            : diderot::tensor<double,3>()
        { }
        tensor_3 (std::initializer_list< double > const & il)
            : diderot::tensor<double,3>(il)
        { }
        tensor_3 (const double *src)
            : diderot::tensor<double,3>(src)
        { }
        tensor_3 (tensor_3 const & ten)
            : diderot::tensor<double,3>(ten._data)
        { }
        ~tensor_3 () { }
        tensor_3 & operator= (tensor_3 const & src);
        tensor_3 & operator= (tensor_ref_3 const & src);
        tensor_3 & operator= (std::initializer_list< double > const & il);
        tensor_3 & operator= (const double *src);
    };
    struct tensor_3_3 : public diderot::tensor<double,9> {
        tensor_3_3 ()
            : diderot::tensor<double,9>()
        { }
        tensor_3_3 (std::initializer_list< double > const & il)
            : diderot::tensor<double,9>(il)
        { }
        tensor_3_3 (const double *src)
            : diderot::tensor<double,9>(src)
        { }
        tensor_3_3 (tensor_3_3 const & ten)
            : diderot::tensor<double,9>(ten._data)
        { }
        ~tensor_3_3 () { }
        tensor_3_3 & operator= (tensor_3_3 const & src);
        tensor_3_3 & operator= (tensor_ref_3_3 const & src);
        tensor_3_3 & operator= (std::initializer_list< double > const & il);
        tensor_3_3 & operator= (const double *src);
        tensor_ref_3 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_2_2 : public diderot::tensor<double,4> {
        tensor_2_2 ()
            : diderot::tensor<double,4>()
        { }
        tensor_2_2 (std::initializer_list< double > const & il)
            : diderot::tensor<double,4>(il)
        { }
        tensor_2_2 (const double *src)
            : diderot::tensor<double,4>(src)
        { }
        tensor_2_2 (tensor_2_2 const & ten)
            : diderot::tensor<double,4>(ten._data)
        { }
        ~tensor_2_2 () { }
        tensor_2_2 & operator= (tensor_2_2 const & src);
        tensor_2_2 & operator= (tensor_ref_2_2 const & src);
        tensor_2_2 & operator= (std::initializer_list< double > const & il);
        tensor_2_2 & operator= (const double *src);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_2_2_4 : public diderot::tensor<double,16> {
        tensor_2_2_4 ()
            : diderot::tensor<double,16>()
        { }
        tensor_2_2_4 (std::initializer_list< double > const & il)
            : diderot::tensor<double,16>(il)
        { }
        tensor_2_2_4 (const double *src)
            : diderot::tensor<double,16>(src)
        { }
        tensor_2_2_4 (tensor_2_2_4 const & ten)
            : diderot::tensor<double,16>(ten._data)
        { }
        ~tensor_2_2_4 () { }
        tensor_2_2_4 & operator= (tensor_2_2_4 const & src);
        tensor_2_2_4 & operator= (tensor_ref_2_2_4 const & src);
        tensor_2_2_4 & operator= (std::initializer_list< double > const & il);
        tensor_2_2_4 & operator= (const double *src);
        tensor_ref_4 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    inline tensor_ref_4::tensor_ref_4 (const double *src)
        : diderot::tensor_ref<double,4>(src)
    { }
    inline tensor_ref_4::tensor_ref_4 (struct tensor_4 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_ref_4::tensor_ref_4 (tensor_ref_4 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_ref_3::tensor_ref_3 (const double *src)
        : diderot::tensor_ref<double,3>(src)
    { }
    inline tensor_ref_3::tensor_ref_3 (struct tensor_3 const & ten)
        : diderot::tensor_ref<double,3>(ten._data)
    { }
    inline tensor_ref_3::tensor_ref_3 (tensor_ref_3 const & ten)
        : diderot::tensor_ref<double,3>(ten._data)
    { }
    inline tensor_ref_2::tensor_ref_2 (const double *src)
        : diderot::tensor_ref<double,2>(src)
    { }
    inline tensor_ref_2::tensor_ref_2 (struct tensor_2 const & ten)
        : diderot::tensor_ref<double,2>(ten._data)
    { }
    inline tensor_ref_2::tensor_ref_2 (tensor_ref_2 const & ten)
        : diderot::tensor_ref<double,2>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (const double *src)
        : diderot::tensor_ref<double,4>(src)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (struct tensor_2_2 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (tensor_ref_2_2 const & ten)
        : diderot::tensor_ref<double,4>(ten._data)
    { }
    inline tensor_ref_3_3::tensor_ref_3_3 (const double *src)
        : diderot::tensor_ref<double,9>(src)
    { }
    inline tensor_ref_3_3::tensor_ref_3_3 (struct tensor_3_3 const & ten)
        : diderot::tensor_ref<double,9>(ten._data)
    { }
    inline tensor_ref_3_3::tensor_ref_3_3 (tensor_ref_3_3 const & ten)
        : diderot::tensor_ref<double,9>(ten._data)
    { }
    inline tensor_ref_2_2_4::tensor_ref_2_2_4 (const double *src)
        : diderot::tensor_ref<double,16>(src)
    { }
    inline tensor_ref_2_2_4::tensor_ref_2_2_4 (struct tensor_2_2_4 const & ten)
        : diderot::tensor_ref<double,16>(ten._data)
    { }
    inline tensor_ref_2_2_4::tensor_ref_2_2_4 (tensor_ref_2_2_4 const & ten)
        : diderot::tensor_ref<double,16>(ten._data)
    { }
    inline tensor_4 & tensor_4::operator= (tensor_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (tensor_ref_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_4 & tensor_4::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_ref_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_3 & tensor_3::operator= (tensor_3 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_3 & tensor_3::operator= (tensor_ref_3 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_3 & tensor_3::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_3 & tensor_3::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_3_3 & tensor_3_3::operator= (tensor_3_3 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_3_3 & tensor_3_3::operator= (tensor_ref_3_3 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_3_3 & tensor_3_3::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_3_3 & tensor_3_3::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_ref_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2_2_4 & tensor_2_2_4::operator= (tensor_2_2_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2_4 & tensor_2_2_4::operator= (tensor_ref_2_2_4 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2_4 & tensor_2_2_4::operator= (std::initializer_list< double > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2_2_4 & tensor_2_2_4::operator= (const double *src)
    {
        this->copy(src);
        return *this;
    }
} // namespace Diderot
// ***** End synthesized types *****

/*---------- begin namespace-open.in ----------*/
namespace Diderot {

static std::string ProgramName = "observ";

struct world;
struct f_strand;
/*---------- end namespace-open.in ----------*/

/*---------- begin nrrd-save-helper.in ----------*/
/* helper function for saving output to nrrd file */
inline bool nrrd_save_helper (std::string const &file, Nrrd *nrrd)
{
    if (nrrdSave (file.c_str(), nrrd, nullptr)) {
        std::cerr << "Error saving \"" << file << "\":\n" << biffGetDone(NRRD) << std::endl;
        return true;
    }
    else {
        return false;
    }
}
/*---------- end nrrd-save-helper.in ----------*/

struct globals {
    diderot::image3d< double, float > gv_promote_img;
    int32_t gv_length;
    tensor_2_2 gv_F0;
    ~globals ()
    {
        this->gv_promote_img.free_data();
    }
};
struct f_strand {
    tensor_2_2_4 sv_out;
    int32_t sv_i;
};
/*---------- begin seq-sarr.in ----------*/
// forward declarations of strand methods
#ifdef DIDEROT_HAS_START_METHOD
static diderot::strand_status f_start (f_strand *self);
#endif // DIDEROT_HAS_START_METHOD
static diderot::strand_status f_update (globals *glob, f_strand *self);
#ifdef DIDEROT_HAS_STABILIZE_METHOD
static void f_stabilize (f_strand *self);
#endif // DIDEROT_HAS_STABILIZE_METHOD

// if we have both communication and "die", then we need to track when strands die
// so that we can rebuild the list of strands use to construct the kd-tree
#if defined(DIDEROT_HAS_STRAND_COMMUNICATION) && !defined(DIDEROT_HAS_STRAND_DIE)
#  define TRACK_STRAND_DEATH
#endif

// strand_array for SEQUENTIAL/NO BSP/SINGLE STATE/DIRECT ACCESS
//
struct strand_array {
    typedef f_strand strand_t;
    typedef uint32_t index_t;
    typedef index_t sid_t;              // strand ID (index into strand-state storage)

    uint8_t             *_status;       // the array of status information for the strands
    char                *_storage;      // points to array of f_strand structs
    uint32_t            _nItems;        // number of items in the _storage and _status arrays
    uint32_t            _nStable;       // number of stable strands
    uint32_t            _nActive;       // number of active strands
    uint32_t            _nFresh;        // number of fresh strands (new strands from create_strands)
#ifdef TRACK_STRAND_DEATH
    bool                _died;          // a strand died in the current superstep.
#endif

    strand_array () : _status(nullptr), _storage(nullptr), _nItems(0) { }
    ~strand_array ();

    uint32_t in_state_index () const { return 0; /* dummy */ }

    uint32_t num_active () const { return this->_nActive; }
    uint32_t num_stable () const { return this->_nStable; }
    uint32_t num_alive () const { return this->_nActive+this->_nStable; }

  // return the ID of a strand, which is the same as the ix index
    sid_t id (index_t ix) const
    {
        assert (ix < this->_nItems);
        return ix;
    }
  // return a pointer to the strand with the given ID
    f_strand *id_to_strand (sid_t id) const
    {
        assert (id < this->_nItems);
        return reinterpret_cast<f_strand *>(this->_storage + id * sizeof(f_strand));
    }

  // return a strand's status
    diderot::strand_status status (index_t ix) const
    {
        assert (ix < this->_nItems);
        return static_cast<diderot::strand_status>(this->_status[ix]);
    }
  // return a pointer to the given strand
    f_strand *strand (index_t ix) const
    {
        return this->id_to_strand(this->id(ix));
    }
  // return a pointer to the local state of strand ix
    f_strand *local_state (index_t ix) const
    {
        return this->strand(ix);
    }
  // return a pointer to the local state of strand with the given ID
    f_strand *id_to_local_state (sid_t id) const
    {
        return this->id_to_strand(id);
    }

  // is an index valid for the strand array?
    bool validIndex (index_t ix) const { return (ix < this->_nItems); }

  // is a given strand alive?
    bool isAlive (index_t ix) const
    {
#ifdef DIDEROT_HAS_STRAND_DIE
        return aliveSts(this->status(ix));
#else
        return true;
#endif
    }

  // allocate space for nItems
    bool alloc (uint32_t nItems)
    {
        this->_storage = static_cast<char *>(std::malloc (nItems * sizeof(f_strand)));
        if (this->_storage == nullptr) {
            return true;
        }
        this->_status = static_cast<uint8_t *>(std::malloc (nItems * sizeof(uint8_t)));
        if (this->_status == nullptr) {
            std::free (this->_storage);
            return true;
        }
        this->_nItems = nItems;
        this->_nActive = 0;
        this->_nStable = 0;
        this->_nFresh = 0;
        return false;
    }

  // initialize the first nStrands locations as new active strands
    void create_strands (uint32_t nStrands)
    {
        assert (this->_nActive == 0);
        assert (this->_nItems == nStrands);
        for (index_t ix = 0;  ix < nStrands;  ix++) {
            this->_status[ix] = diderot::kActive;
            new (this->strand(ix)) f_strand;
        }
        this->_nActive = nStrands;
        this->_nFresh = nStrands;
#ifdef TRACK_STRAND_DEATH
        this->_died = false;
#endif
    }

  // swap in and out states (NOP for this version)
    void swap () { }

#ifdef DIDEROT_HAS_START_METHOD
  // invoke strand's start method
    diderot::strand_status strand_start (index_t ix)
    {
        return f_start(this->strand(ix));
    }
#endif // DIDEROT_HAS_START_METHOD

  // invoke strand's update method
    diderot::strand_status strand_update (globals *glob, index_t ix)
    {
        return f_update(glob, this->strand(ix));
    }

  // invoke strand's stabilize method
    index_t strand_stabilize (index_t ix)
    {
#ifdef DIDEROT_HAS_STABILIZE_METHOD
        f_stabilize (this->strand(ix));
#endif // DIDEROT_HAS_STABILIZE_METHOD
        this->_status[ix] = diderot::kStable;
        this->_nActive--;
        this->_nStable++;
      // skip to next active strand
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // mark the given strand as dead
    index_t kill (index_t ix)
    {
#ifdef TRACK_STRAND_DEATH
        this->_died = true;
#endif
        this->_status[ix] = diderot::kDead;
        this->_nActive--;
      // skip to next active strand
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // finish the local-phase of a superstep (NOP)
#ifdef TRACK_STRAND_DEATH
    bool finish_step ()
    {
        bool res = this->_died;
        this->_died = false;
        return res;
    }
#else
    bool finish_step () { return false; }
#endif

  // finish a kill_all operation (NOP)
    void finish_kill_all () { }

  // finish a stabilize_all operation (NOP)
    void finish_stabilize_all () { }

    index_t begin_alive () const
    {
        index_t ix = 0;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && notAliveSts(this->status(ix))) {
            ix++;
        }
#endif
        return ix;
    }
    index_t end_alive () const { return this->_nItems; }
    index_t next_alive (index_t &ix) const
    {
        ix++;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && notAliveSts(this->status(ix))) {
            ix++;
        }
#endif
        return ix;
    }

  // iterator over active strands
    index_t begin_active () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && notActiveSts(this->status(ix))) {
            ix++;
        }
        return ix;
    }
    index_t end_active () const { return this->_nItems; }
    index_t next_active (index_t &ix) const
    {
        do {
            ix++;
        } while ((ix < this->_nItems) && notActiveSts(this->status(ix)));
        return ix;
    }

  // iterator over stable strands
    index_t begin_stable () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->status(ix) != diderot::kStable)) {
            ix++;
        }
        return ix;
    }
    index_t end_stable () const { return this->_nItems; }
    index_t next_stable (index_t &ix) const
    {
        do {
            ix++;
        } while ((ix < this->_nItems) && (this->status(ix) != diderot::kStable));
        return ix;
    }

  // iterator over fresh strands; since the only new strands were created by create_strand
  // we iterate over all of them
    index_t begin_fresh () const { return 0; }
    index_t end_fresh () const { return this->_nFresh; }
    index_t next_fresh (index_t &ix) const { return ++ix; }

}; // struct strand_array

strand_array::~strand_array ()
{
  // run destructors to reclaim any dynamic memory attached to the strand state
    for (auto ix = this->begin_alive();  ix != this->end_alive();  ix = this->next_alive(ix)) {
        this->strand(ix)->~f_strand();
    }
    if (this->_status != nullptr) std::free (this->_status);
    if (this->_storage != nullptr) std::free (this->_storage);
}
/*---------- end seq-sarr.in ----------*/

struct world : public diderot::world_base {
    strand_array _strands;
    globals *_globals;
    world ();
    ~world ();
    bool init ();
    bool alloc (int32_t base[1], uint32_t size[1]);
    bool create_strands ();
    uint32_t run (uint32_t max_nsteps);
    void swap_state ();
};
// ***** Begin synthesized operations *****

inline vec3 vfloor3 (vec3 v)
{
    return __extension__ (vec3){diderot::floor(v[0]), diderot::floor(v[1]), diderot::floor(v[2]), 0.0};
}
inline double vdot6 (vec6 u, vec6 v)
{
    vec6 w = u * v;
    return w[0] + w[1] + w[2] + w[3] + w[4] + w[5];
}
inline diderot::array< int, 3 > vtoi3 (vec3 src)
{
    diderot::array< int, 3 > res = {int32_t(src[0]),int32_t(src[1]),int32_t(src[2]),};
    return res;
}
inline vec3 vload3 (const double *vp)
{
    return __extension__ (vec3){vp[0], vp[1], vp[2], 0.0};
}
inline vec3 vcons3 (double r0, double r1, double r2)
{
    return __extension__ (vec3){r0, r1, r2, 0.0};
}
template <typename TY>
inline bool inside3Ds3 (vec3 x0, diderot::image3d< double, TY > img)
{
    return 2 < x0[0] && x0[2] < img.size(2) - 3 && 2 < x0[2] && x0[1] < img.size(1) - 3 && 2 < x0[1] && x0[0] < img.size(
        0) - 3;
}
template <typename TY>
inline tensor_ref_3_3 world2image (diderot::image3d< double, TY > const & img)
{
    return tensor_ref_3_3(img.world2image());
}
inline vec6 vcons6 (double r0, double r1, double r2, double r3, double r4, double r5)
{
    return __extension__ (vec6){r0, r1, r2, r3, r4, r5, 0.0, 0.0};
}
inline double vdot3 (vec3 u, vec3 v)
{
    vec3 w = u * v;
    return w[0] + w[1] + w[2];
}
template <typename TY>
inline tensor_ref_3 translate (diderot::image3d< double, TY > const & img)
{
    return tensor_ref_3(img.translate());
}
// ***** End synthesized operations *****

static std::string OutputFile = "out.nrrd";
static void register_outputs (diderot::options *opts)
{
    opts->add("o,output", "specify output file", &OutputFile, true);
}
static bool init_globals (world *wrld)
{
    diderot::image3d< double, float > l_promote_img_0;
    globals *glob = wrld->_globals;
    if (l_promote_img_0.load(wrld, "inputfile1.nrrd")) {
        return true;
    }
    glob->gv_promote_img = l_promote_img_0;
    glob->gv_length = 7;
    glob->gv_F0[0] = 0.2e1;
    glob->gv_F0[1] = -0.1e1;
    glob->gv_F0[2] = 0.2e1;
    glob->gv_F0[3] = 0.4e1;
    return false;
}
static void f_init (f_strand *self, int32_t p_i_1)
{
    self->sv_out[0] = 0.0;
    self->sv_out[1] = 0.0;
    self->sv_out[2] = 0.0;
    self->sv_out[3] = 0.0;
    self->sv_out[4] = 0.0;
    self->sv_out[5] = 0.0;
    self->sv_out[6] = 0.0;
    self->sv_out[7] = 0.0;
    self->sv_out[8] = 0.0;
    self->sv_out[9] = 0.0;
    self->sv_out[10] = 0.0;
    self->sv_out[11] = 0.0;
    self->sv_out[12] = 0.0;
    self->sv_out[13] = 0.0;
    self->sv_out[14] = 0.0;
    self->sv_out[15] = 0.0;
    self->sv_i = p_i_1;
}
static diderot::strand_status f_update (globals *glob, f_strand *self)
{
    vec3 v_3;
    bool l__t_14;
    tensor_2_2_4 l_out_313;
    vec3 v_2 = vcons3(0.0, 0.0, 0.0);
    if (self->sv_i == 0) {
        v_3 = vcons3(0.32e0, 0.21e0, -0.16e0);
    }
    else {
        vec3 v_4;
        if (self->sv_i == 1) {
            v_4 = vcons3(0.32e0, 0.21e0, -0.16e0);
        }
        else {
            vec3 v_5;
            if (self->sv_i == 2) {
                v_5 = vcons3(-0.17e0, 0.3e-1, -0.25e0);
            }
            else {
                vec3 v_6;
                if (self->sv_i == 3) {
                    v_6 = vcons3(0.0, -0.35e0, -0.33e0);
                }
                else {
                    vec3 v_7;
                    if (self->sv_i == 4) {
                        v_7 = vcons3(-0.22e0, 0.39e0, -0.5e-1);
                    }
                    else {
                        vec3 v_8;
                        if (self->sv_i == 5) {
                            v_8 = vcons3(0.18e0, 0.7e-1, -0.11e0);
                        }
                        else {
                            vec3 v_9;
                            if (self->sv_i == 6) {
                                v_9 = vcons3(-0.6e-1, 0.4e-1, -0.24e0);
                            }
                            else {
                                vec3 v_10;
                                if (self->sv_i == 7) {
                                    v_10 = vcons3(-0.33e0, -0.0, 0.8e-1);
                                }
                                else {
                                    v_10 = v_2;
                                }
                                v_9 = v_10;
                            }
                            v_8 = v_9;
                        }
                        v_7 = v_8;
                    }
                    v_6 = v_7;
                }
                v_5 = v_6;
            }
            v_4 = v_5;
        }
        v_3 = v_4;
    }
    tensor_ref_3_3 l_Mtransform_11 = world2image(glob->gv_promote_img);
    vec3 v_12 = vcons3(vdot3(vload3(l_Mtransform_11.last(0).addr(0)), v_3),
        vdot3(vload3(l_Mtransform_11.last(3).addr(0)), v_3), vdot3(vload3(l_Mtransform_11.last(6).addr(0)), v_3)) + vload3(
        translate(glob->gv_promote_img).addr(0));
    vec3 v_13 = v_12;
    if (inside3Ds3(v_12, glob->gv_promote_img)) {
        l__t_14 = true;
    }
    else {
        l__t_14 = false;
    }
    if (l__t_14) {
        vec3 v_15 = vfloor3(v_13);
        vec3 v_16 = v_13 - v_15;
        diderot::array< int32_t, 3 > l_n_17 = vtoi3(v_15);
        int32_t l_idx_18 = l_n_17[0] + -2;
        int32_t l_idx_19 = l_n_17[1] + -2;
        int32_t l_idx_20 = l_n_17[2] + -2;
        int32_t l_mulRes_21 = 70 * l_idx_20;
        int32_t l_mulRes_22 = 70 * (l_idx_19 + l_mulRes_21);
        int32_t l_offp_23 = 4 * (l_idx_18 + l_mulRes_22);
        int32_t l_addRes_24 = l_idx_18 + 1;
        int32_t l_offp_25 = 4 * (l_addRes_24 + l_mulRes_22);
        int32_t l_addRes_26 = l_idx_18 + 2;
        int32_t l_offp_27 = 4 * (l_addRes_26 + l_mulRes_22);
        int32_t l_addRes_28 = l_idx_18 + 3;
        int32_t l_offp_29 = 4 * (l_addRes_28 + l_mulRes_22);
        int32_t l_addRes_30 = l_idx_18 + 4;
        int32_t l_offp_31 = 4 * (l_addRes_30 + l_mulRes_22);
        int32_t l_addRes_32 = l_idx_18 + 5;
        int32_t l_offp_33 = 4 * (l_addRes_32 + l_mulRes_22);
        int32_t l_addRes_34 = l_idx_19 + 1;
        int32_t l_mulRes_35 = 70 * (l_addRes_34 + l_mulRes_21);
        int32_t l_offp_36 = 4 * (l_idx_18 + l_mulRes_35);
        int32_t l_offp_37 = 4 * (l_addRes_24 + l_mulRes_35);
        int32_t l_offp_38 = 4 * (l_addRes_26 + l_mulRes_35);
        int32_t l_offp_39 = 4 * (l_addRes_28 + l_mulRes_35);
        int32_t l_offp_40 = 4 * (l_addRes_30 + l_mulRes_35);
        int32_t l_offp_41 = 4 * (l_addRes_32 + l_mulRes_35);
        int32_t l_addRes_42 = l_idx_19 + 2;
        int32_t l_mulRes_43 = 70 * (l_addRes_42 + l_mulRes_21);
        int32_t l_offp_44 = 4 * (l_idx_18 + l_mulRes_43);
        int32_t l_offp_45 = 4 * (l_addRes_24 + l_mulRes_43);
        int32_t l_offp_46 = 4 * (l_addRes_26 + l_mulRes_43);
        int32_t l_offp_47 = 4 * (l_addRes_28 + l_mulRes_43);
        int32_t l_offp_48 = 4 * (l_addRes_30 + l_mulRes_43);
        int32_t l_offp_49 = 4 * (l_addRes_32 + l_mulRes_43);
        int32_t l_addRes_50 = l_idx_19 + 3;
        int32_t l_mulRes_51 = 70 * (l_addRes_50 + l_mulRes_21);
        int32_t l_offp_52 = 4 * (l_idx_18 + l_mulRes_51);
        int32_t l_offp_53 = 4 * (l_addRes_24 + l_mulRes_51);
        int32_t l_offp_54 = 4 * (l_addRes_26 + l_mulRes_51);
        int32_t l_offp_55 = 4 * (l_addRes_28 + l_mulRes_51);
        int32_t l_offp_56 = 4 * (l_addRes_30 + l_mulRes_51);
        int32_t l_offp_57 = 4 * (l_addRes_32 + l_mulRes_51);
        int32_t l_addRes_58 = l_idx_19 + 4;
        int32_t l_mulRes_59 = 70 * (l_addRes_58 + l_mulRes_21);
        int32_t l_offp_60 = 4 * (l_idx_18 + l_mulRes_59);
        int32_t l_offp_61 = 4 * (l_addRes_24 + l_mulRes_59);
        int32_t l_offp_62 = 4 * (l_addRes_26 + l_mulRes_59);
        int32_t l_offp_63 = 4 * (l_addRes_28 + l_mulRes_59);
        int32_t l_offp_64 = 4 * (l_addRes_30 + l_mulRes_59);
        int32_t l_offp_65 = 4 * (l_addRes_32 + l_mulRes_59);
        int32_t l_addRes_66 = l_idx_19 + 5;
        int32_t l_mulRes_67 = 70 * (l_addRes_66 + l_mulRes_21);
        int32_t l_offp_68 = 4 * (l_idx_18 + l_mulRes_67);
        int32_t l_offp_69 = 4 * (l_addRes_24 + l_mulRes_67);
        int32_t l_offp_70 = 4 * (l_addRes_26 + l_mulRes_67);
        int32_t l_offp_71 = 4 * (l_addRes_28 + l_mulRes_67);
        int32_t l_offp_72 = 4 * (l_addRes_30 + l_mulRes_67);
        int32_t l_offp_73 = 4 * (l_addRes_32 + l_mulRes_67);
        int32_t l_mulRes_74 = 70 * (l_idx_20 + 1);
        int32_t l_mulRes_75 = 70 * (l_idx_19 + l_mulRes_74);
        int32_t l_offp_76 = 4 * (l_idx_18 + l_mulRes_75);
        int32_t l_offp_77 = 4 * (l_addRes_24 + l_mulRes_75);
        int32_t l_offp_78 = 4 * (l_addRes_26 + l_mulRes_75);
        int32_t l_offp_79 = 4 * (l_addRes_28 + l_mulRes_75);
        int32_t l_offp_80 = 4 * (l_addRes_30 + l_mulRes_75);
        int32_t l_offp_81 = 4 * (l_addRes_32 + l_mulRes_75);
        int32_t l_mulRes_82 = 70 * (l_addRes_34 + l_mulRes_74);
        int32_t l_offp_83 = 4 * (l_idx_18 + l_mulRes_82);
        int32_t l_offp_84 = 4 * (l_addRes_24 + l_mulRes_82);
        int32_t l_offp_85 = 4 * (l_addRes_26 + l_mulRes_82);
        int32_t l_offp_86 = 4 * (l_addRes_28 + l_mulRes_82);
        int32_t l_offp_87 = 4 * (l_addRes_30 + l_mulRes_82);
        int32_t l_offp_88 = 4 * (l_addRes_32 + l_mulRes_82);
        int32_t l_mulRes_89 = 70 * (l_addRes_42 + l_mulRes_74);
        int32_t l_offp_90 = 4 * (l_idx_18 + l_mulRes_89);
        int32_t l_offp_91 = 4 * (l_addRes_24 + l_mulRes_89);
        int32_t l_offp_92 = 4 * (l_addRes_26 + l_mulRes_89);
        int32_t l_offp_93 = 4 * (l_addRes_28 + l_mulRes_89);
        int32_t l_offp_94 = 4 * (l_addRes_30 + l_mulRes_89);
        int32_t l_offp_95 = 4 * (l_addRes_32 + l_mulRes_89);
        int32_t l_mulRes_96 = 70 * (l_addRes_50 + l_mulRes_74);
        int32_t l_offp_97 = 4 * (l_idx_18 + l_mulRes_96);
        int32_t l_offp_98 = 4 * (l_addRes_24 + l_mulRes_96);
        int32_t l_offp_99 = 4 * (l_addRes_26 + l_mulRes_96);
        int32_t l_offp_100 = 4 * (l_addRes_28 + l_mulRes_96);
        int32_t l_offp_101 = 4 * (l_addRes_30 + l_mulRes_96);
        int32_t l_offp_102 = 4 * (l_addRes_32 + l_mulRes_96);
        int32_t l_mulRes_103 = 70 * (l_addRes_58 + l_mulRes_74);
        int32_t l_offp_104 = 4 * (l_idx_18 + l_mulRes_103);
        int32_t l_offp_105 = 4 * (l_addRes_24 + l_mulRes_103);
        int32_t l_offp_106 = 4 * (l_addRes_26 + l_mulRes_103);
        int32_t l_offp_107 = 4 * (l_addRes_28 + l_mulRes_103);
        int32_t l_offp_108 = 4 * (l_addRes_30 + l_mulRes_103);
        int32_t l_offp_109 = 4 * (l_addRes_32 + l_mulRes_103);
        int32_t l_mulRes_110 = 70 * (l_addRes_66 + l_mulRes_74);
        int32_t l_offp_111 = 4 * (l_idx_18 + l_mulRes_110);
        int32_t l_offp_112 = 4 * (l_addRes_24 + l_mulRes_110);
        int32_t l_offp_113 = 4 * (l_addRes_26 + l_mulRes_110);
        int32_t l_offp_114 = 4 * (l_addRes_28 + l_mulRes_110);
        int32_t l_offp_115 = 4 * (l_addRes_30 + l_mulRes_110);
        int32_t l_offp_116 = 4 * (l_addRes_32 + l_mulRes_110);
        int32_t l_mulRes_117 = 70 * (l_idx_20 + 2);
        int32_t l_mulRes_118 = 70 * (l_idx_19 + l_mulRes_117);
        int32_t l_offp_119 = 4 * (l_idx_18 + l_mulRes_118);
        int32_t l_offp_120 = 4 * (l_addRes_24 + l_mulRes_118);
        int32_t l_offp_121 = 4 * (l_addRes_26 + l_mulRes_118);
        int32_t l_offp_122 = 4 * (l_addRes_28 + l_mulRes_118);
        int32_t l_offp_123 = 4 * (l_addRes_30 + l_mulRes_118);
        int32_t l_offp_124 = 4 * (l_addRes_32 + l_mulRes_118);
        int32_t l_mulRes_125 = 70 * (l_addRes_34 + l_mulRes_117);
        int32_t l_offp_126 = 4 * (l_idx_18 + l_mulRes_125);
        int32_t l_offp_127 = 4 * (l_addRes_24 + l_mulRes_125);
        int32_t l_offp_128 = 4 * (l_addRes_26 + l_mulRes_125);
        int32_t l_offp_129 = 4 * (l_addRes_28 + l_mulRes_125);
        int32_t l_offp_130 = 4 * (l_addRes_30 + l_mulRes_125);
        int32_t l_offp_131 = 4 * (l_addRes_32 + l_mulRes_125);
        int32_t l_mulRes_132 = 70 * (l_addRes_42 + l_mulRes_117);
        int32_t l_offp_133 = 4 * (l_idx_18 + l_mulRes_132);
        int32_t l_offp_134 = 4 * (l_addRes_24 + l_mulRes_132);
        int32_t l_offp_135 = 4 * (l_addRes_26 + l_mulRes_132);
        int32_t l_offp_136 = 4 * (l_addRes_28 + l_mulRes_132);
        int32_t l_offp_137 = 4 * (l_addRes_30 + l_mulRes_132);
        int32_t l_offp_138 = 4 * (l_addRes_32 + l_mulRes_132);
        int32_t l_mulRes_139 = 70 * (l_addRes_50 + l_mulRes_117);
        int32_t l_offp_140 = 4 * (l_idx_18 + l_mulRes_139);
        int32_t l_offp_141 = 4 * (l_addRes_24 + l_mulRes_139);
        int32_t l_offp_142 = 4 * (l_addRes_26 + l_mulRes_139);
        int32_t l_offp_143 = 4 * (l_addRes_28 + l_mulRes_139);
        int32_t l_offp_144 = 4 * (l_addRes_30 + l_mulRes_139);
        int32_t l_offp_145 = 4 * (l_addRes_32 + l_mulRes_139);
        int32_t l_mulRes_146 = 70 * (l_addRes_58 + l_mulRes_117);
        int32_t l_offp_147 = 4 * (l_idx_18 + l_mulRes_146);
        int32_t l_offp_148 = 4 * (l_addRes_24 + l_mulRes_146);
        int32_t l_offp_149 = 4 * (l_addRes_26 + l_mulRes_146);
        int32_t l_offp_150 = 4 * (l_addRes_28 + l_mulRes_146);
        int32_t l_offp_151 = 4 * (l_addRes_30 + l_mulRes_146);
        int32_t l_offp_152 = 4 * (l_addRes_32 + l_mulRes_146);
        int32_t l_mulRes_153 = 70 * (l_addRes_66 + l_mulRes_117);
        int32_t l_offp_154 = 4 * (l_idx_18 + l_mulRes_153);
        int32_t l_offp_155 = 4 * (l_addRes_24 + l_mulRes_153);
        int32_t l_offp_156 = 4 * (l_addRes_26 + l_mulRes_153);
        int32_t l_offp_157 = 4 * (l_addRes_28 + l_mulRes_153);
        int32_t l_offp_158 = 4 * (l_addRes_30 + l_mulRes_153);
        int32_t l_offp_159 = 4 * (l_addRes_32 + l_mulRes_153);
        int32_t l_mulRes_160 = 70 * (l_idx_20 + 3);
        int32_t l_mulRes_161 = 70 * (l_idx_19 + l_mulRes_160);
        int32_t l_offp_162 = 4 * (l_idx_18 + l_mulRes_161);
        int32_t l_offp_163 = 4 * (l_addRes_24 + l_mulRes_161);
        int32_t l_offp_164 = 4 * (l_addRes_26 + l_mulRes_161);
        int32_t l_offp_165 = 4 * (l_addRes_28 + l_mulRes_161);
        int32_t l_offp_166 = 4 * (l_addRes_30 + l_mulRes_161);
        int32_t l_offp_167 = 4 * (l_addRes_32 + l_mulRes_161);
        int32_t l_mulRes_168 = 70 * (l_addRes_34 + l_mulRes_160);
        int32_t l_offp_169 = 4 * (l_idx_18 + l_mulRes_168);
        int32_t l_offp_170 = 4 * (l_addRes_24 + l_mulRes_168);
        int32_t l_offp_171 = 4 * (l_addRes_26 + l_mulRes_168);
        int32_t l_offp_172 = 4 * (l_addRes_28 + l_mulRes_168);
        int32_t l_offp_173 = 4 * (l_addRes_30 + l_mulRes_168);
        int32_t l_offp_174 = 4 * (l_addRes_32 + l_mulRes_168);
        int32_t l_mulRes_175 = 70 * (l_addRes_42 + l_mulRes_160);
        int32_t l_offp_176 = 4 * (l_idx_18 + l_mulRes_175);
        int32_t l_offp_177 = 4 * (l_addRes_24 + l_mulRes_175);
        int32_t l_offp_178 = 4 * (l_addRes_26 + l_mulRes_175);
        int32_t l_offp_179 = 4 * (l_addRes_28 + l_mulRes_175);
        int32_t l_offp_180 = 4 * (l_addRes_30 + l_mulRes_175);
        int32_t l_offp_181 = 4 * (l_addRes_32 + l_mulRes_175);
        int32_t l_mulRes_182 = 70 * (l_addRes_50 + l_mulRes_160);
        int32_t l_offp_183 = 4 * (l_idx_18 + l_mulRes_182);
        int32_t l_offp_184 = 4 * (l_addRes_24 + l_mulRes_182);
        int32_t l_offp_185 = 4 * (l_addRes_26 + l_mulRes_182);
        int32_t l_offp_186 = 4 * (l_addRes_28 + l_mulRes_182);
        int32_t l_offp_187 = 4 * (l_addRes_30 + l_mulRes_182);
        int32_t l_offp_188 = 4 * (l_addRes_32 + l_mulRes_182);
        int32_t l_mulRes_189 = 70 * (l_addRes_58 + l_mulRes_160);
        int32_t l_offp_190 = 4 * (l_idx_18 + l_mulRes_189);
        int32_t l_offp_191 = 4 * (l_addRes_24 + l_mulRes_189);
        int32_t l_offp_192 = 4 * (l_addRes_26 + l_mulRes_189);
        int32_t l_offp_193 = 4 * (l_addRes_28 + l_mulRes_189);
        int32_t l_offp_194 = 4 * (l_addRes_30 + l_mulRes_189);
        int32_t l_offp_195 = 4 * (l_addRes_32 + l_mulRes_189);
        int32_t l_mulRes_196 = 70 * (l_addRes_66 + l_mulRes_160);
        int32_t l_offp_197 = 4 * (l_idx_18 + l_mulRes_196);
        int32_t l_offp_198 = 4 * (l_addRes_24 + l_mulRes_196);
        int32_t l_offp_199 = 4 * (l_addRes_26 + l_mulRes_196);
        int32_t l_offp_200 = 4 * (l_addRes_28 + l_mulRes_196);
        int32_t l_offp_201 = 4 * (l_addRes_30 + l_mulRes_196);
        int32_t l_offp_202 = 4 * (l_addRes_32 + l_mulRes_196);
        int32_t l_mulRes_203 = 70 * (l_idx_20 + 4);
        int32_t l_mulRes_204 = 70 * (l_idx_19 + l_mulRes_203);
        int32_t l_offp_205 = 4 * (l_idx_18 + l_mulRes_204);
        int32_t l_offp_206 = 4 * (l_addRes_24 + l_mulRes_204);
        int32_t l_offp_207 = 4 * (l_addRes_26 + l_mulRes_204);
        int32_t l_offp_208 = 4 * (l_addRes_28 + l_mulRes_204);
        int32_t l_offp_209 = 4 * (l_addRes_30 + l_mulRes_204);
        int32_t l_offp_210 = 4 * (l_addRes_32 + l_mulRes_204);
        int32_t l_mulRes_211 = 70 * (l_addRes_34 + l_mulRes_203);
        int32_t l_offp_212 = 4 * (l_idx_18 + l_mulRes_211);
        int32_t l_offp_213 = 4 * (l_addRes_24 + l_mulRes_211);
        int32_t l_offp_214 = 4 * (l_addRes_26 + l_mulRes_211);
        int32_t l_offp_215 = 4 * (l_addRes_28 + l_mulRes_211);
        int32_t l_offp_216 = 4 * (l_addRes_30 + l_mulRes_211);
        int32_t l_offp_217 = 4 * (l_addRes_32 + l_mulRes_211);
        int32_t l_mulRes_218 = 70 * (l_addRes_42 + l_mulRes_203);
        int32_t l_offp_219 = 4 * (l_idx_18 + l_mulRes_218);
        int32_t l_offp_220 = 4 * (l_addRes_24 + l_mulRes_218);
        int32_t l_offp_221 = 4 * (l_addRes_26 + l_mulRes_218);
        int32_t l_offp_222 = 4 * (l_addRes_28 + l_mulRes_218);
        int32_t l_offp_223 = 4 * (l_addRes_30 + l_mulRes_218);
        int32_t l_offp_224 = 4 * (l_addRes_32 + l_mulRes_218);
        int32_t l_mulRes_225 = 70 * (l_addRes_50 + l_mulRes_203);
        int32_t l_offp_226 = 4 * (l_idx_18 + l_mulRes_225);
        int32_t l_offp_227 = 4 * (l_addRes_24 + l_mulRes_225);
        int32_t l_offp_228 = 4 * (l_addRes_26 + l_mulRes_225);
        int32_t l_offp_229 = 4 * (l_addRes_28 + l_mulRes_225);
        int32_t l_offp_230 = 4 * (l_addRes_30 + l_mulRes_225);
        int32_t l_offp_231 = 4 * (l_addRes_32 + l_mulRes_225);
        int32_t l_mulRes_232 = 70 * (l_addRes_58 + l_mulRes_203);
        int32_t l_offp_233 = 4 * (l_idx_18 + l_mulRes_232);
        int32_t l_offp_234 = 4 * (l_addRes_24 + l_mulRes_232);
        int32_t l_offp_235 = 4 * (l_addRes_26 + l_mulRes_232);
        int32_t l_offp_236 = 4 * (l_addRes_28 + l_mulRes_232);
        int32_t l_offp_237 = 4 * (l_addRes_30 + l_mulRes_232);
        int32_t l_offp_238 = 4 * (l_addRes_32 + l_mulRes_232);
        int32_t l_mulRes_239 = 70 * (l_addRes_66 + l_mulRes_203);
        int32_t l_offp_240 = 4 * (l_idx_18 + l_mulRes_239);
        int32_t l_offp_241 = 4 * (l_addRes_24 + l_mulRes_239);
        int32_t l_offp_242 = 4 * (l_addRes_26 + l_mulRes_239);
        int32_t l_offp_243 = 4 * (l_addRes_28 + l_mulRes_239);
        int32_t l_offp_244 = 4 * (l_addRes_30 + l_mulRes_239);
        int32_t l_offp_245 = 4 * (l_addRes_32 + l_mulRes_239);
        int32_t l_mulRes_246 = 70 * (l_idx_20 + 5);
        int32_t l_mulRes_247 = 70 * (l_idx_19 + l_mulRes_246);
        int32_t l_offp_248 = 4 * (l_idx_18 + l_mulRes_247);
        int32_t l_offp_249 = 4 * (l_addRes_24 + l_mulRes_247);
        int32_t l_offp_250 = 4 * (l_addRes_26 + l_mulRes_247);
        int32_t l_offp_251 = 4 * (l_addRes_28 + l_mulRes_247);
        int32_t l_offp_252 = 4 * (l_addRes_30 + l_mulRes_247);
        int32_t l_offp_253 = 4 * (l_addRes_32 + l_mulRes_247);
        int32_t l_mulRes_254 = 70 * (l_addRes_34 + l_mulRes_246);
        int32_t l_offp_255 = 4 * (l_idx_18 + l_mulRes_254);
        int32_t l_offp_256 = 4 * (l_addRes_24 + l_mulRes_254);
        int32_t l_offp_257 = 4 * (l_addRes_26 + l_mulRes_254);
        int32_t l_offp_258 = 4 * (l_addRes_28 + l_mulRes_254);
        int32_t l_offp_259 = 4 * (l_addRes_30 + l_mulRes_254);
        int32_t l_offp_260 = 4 * (l_addRes_32 + l_mulRes_254);
        int32_t l_mulRes_261 = 70 * (l_addRes_42 + l_mulRes_246);
        int32_t l_offp_262 = 4 * (l_idx_18 + l_mulRes_261);
        int32_t l_offp_263 = 4 * (l_addRes_24 + l_mulRes_261);
        int32_t l_offp_264 = 4 * (l_addRes_26 + l_mulRes_261);
        int32_t l_offp_265 = 4 * (l_addRes_28 + l_mulRes_261);
        int32_t l_offp_266 = 4 * (l_addRes_30 + l_mulRes_261);
        int32_t l_offp_267 = 4 * (l_addRes_32 + l_mulRes_261);
        int32_t l_mulRes_268 = 70 * (l_addRes_50 + l_mulRes_246);
        int32_t l_offp_269 = 4 * (l_idx_18 + l_mulRes_268);
        int32_t l_offp_270 = 4 * (l_addRes_24 + l_mulRes_268);
        int32_t l_offp_271 = 4 * (l_addRes_26 + l_mulRes_268);
        int32_t l_offp_272 = 4 * (l_addRes_28 + l_mulRes_268);
        int32_t l_offp_273 = 4 * (l_addRes_30 + l_mulRes_268);
        int32_t l_offp_274 = 4 * (l_addRes_32 + l_mulRes_268);
        int32_t l_mulRes_275 = 70 * (l_addRes_58 + l_mulRes_246);
        int32_t l_offp_276 = 4 * (l_idx_18 + l_mulRes_275);
        int32_t l_offp_277 = 4 * (l_addRes_24 + l_mulRes_275);
        int32_t l_offp_278 = 4 * (l_addRes_26 + l_mulRes_275);
        int32_t l_offp_279 = 4 * (l_addRes_28 + l_mulRes_275);
        int32_t l_offp_280 = 4 * (l_addRes_30 + l_mulRes_275);
        int32_t l_offp_281 = 4 * (l_addRes_32 + l_mulRes_275);
        int32_t l_mulRes_282 = 70 * (l_addRes_66 + l_mulRes_246);
        int32_t l_offp_283 = 4 * (l_idx_18 + l_mulRes_282);
        int32_t l_offp_284 = 4 * (l_addRes_24 + l_mulRes_282);
        int32_t l_offp_285 = 4 * (l_addRes_26 + l_mulRes_282);
        int32_t l_offp_286 = 4 * (l_addRes_28 + l_mulRes_282);
        int32_t l_offp_287 = 4 * (l_addRes_30 + l_mulRes_282);
        int32_t l_offp_288 = 4 * (l_addRes_32 + l_mulRes_282);
        double l_vZ__289 = v_16[2];
        vec6 v_290 = vcons6(l_vZ__289 + 0.2e1, l_vZ__289 + 0.1e1, l_vZ__289, l_vZ__289 - 0.1e1, l_vZ__289 - 0.2e1,
            l_vZ__289 - 0.3e1);
        vec6 v_291 = vcons6(0.961875e1, 0.1875e-1, 0.8625e0, 0.8625e0, 0.1875e-1, 0.961875e1);
        vec6 v_292 = vcons6(-0.23625e2, 0.4375e1, 0.0, 0.0, -0.4375e1, 0.23625e2);
        vec6 v_293 = vcons6(0.2334375e2, -0.1065625e2, -0.14375e1, -0.14375e1, -0.1065625e2, 0.2334375e2);
        vec6 v_294 = vcons6(-0.12e2, 0.10e2, 0.0, 0.0, -0.10e2, 0.12e2);
        vec6 v_295 = vcons6(0.340625e1, -0.459375e1, 0.11875e1, 0.11875e1, -0.459375e1, 0.340625e1);
        vec6 v_296 = vcons6(-0.508333333333e0, 0.104166666667e1, -0.583333333333e0, 0.583333333333e0,
            -0.104166666667e1, 0.508333333333e0);
        vec6 v_297 = vcons6(0.3125e-1, -0.9375e-1, 0.625e-1, 0.625e-1, -0.9375e-1, 0.3125e-1);
        vec6 v_298 = v_291 + v_290 * (v_292 + v_290 * (v_293 + v_290 * (v_294 + v_290 * (v_295 + v_290 * (v_296 + v_290 * v_297)))));
        double l_vY__299 = v_16[1];
        vec6 v_300 = vcons6(l_vY__299 + 0.2e1, l_vY__299 + 0.1e1, l_vY__299, l_vY__299 - 0.1e1, l_vY__299 - 0.2e1,
            l_vY__299 - 0.3e1);
        vec6 v_301 = v_291 + v_300 * (v_292 + v_300 * (v_293 + v_300 * (v_294 + v_300 * (v_295 + v_300 * (v_296 + v_300 * v_297)))));
        double l_vX__302 = v_16[0];
        vec6 v_303 = vcons6(l_vX__302 + 0.2e1, l_vX__302 + 0.1e1, l_vX__302, l_vX__302 - 0.1e1, l_vX__302 - 0.2e1,
            l_vX__302 - 0.3e1);
        vec6 v_304 = v_291 + v_303 * (v_292 + v_303 * (v_293 + v_303 * (v_294 + v_303 * (v_295 + v_303 * (v_296 + v_303 * v_297)))));
        double l_vdot_305 = vdot6(v_298,
            vcons6(
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_23]),
                                static_cast<double>(glob->gv_promote_img[l_offp_25]),
                                static_cast<double>(glob->gv_promote_img[l_offp_27]),
                                static_cast<double>(glob->gv_promote_img[l_offp_29]),
                                static_cast<double>(glob->gv_promote_img[l_offp_31]),
                                static_cast<double>(glob->gv_promote_img[l_offp_33]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_36]),
                                static_cast<double>(glob->gv_promote_img[l_offp_37]),
                                static_cast<double>(glob->gv_promote_img[l_offp_38]),
                                static_cast<double>(glob->gv_promote_img[l_offp_39]),
                                static_cast<double>(glob->gv_promote_img[l_offp_40]),
                                static_cast<double>(glob->gv_promote_img[l_offp_41]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_44]),
                                static_cast<double>(glob->gv_promote_img[l_offp_45]),
                                static_cast<double>(glob->gv_promote_img[l_offp_46]),
                                static_cast<double>(glob->gv_promote_img[l_offp_47]),
                                static_cast<double>(glob->gv_promote_img[l_offp_48]),
                                static_cast<double>(glob->gv_promote_img[l_offp_49]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_52]),
                                static_cast<double>(glob->gv_promote_img[l_offp_53]),
                                static_cast<double>(glob->gv_promote_img[l_offp_54]),
                                static_cast<double>(glob->gv_promote_img[l_offp_55]),
                                static_cast<double>(glob->gv_promote_img[l_offp_56]),
                                static_cast<double>(glob->gv_promote_img[l_offp_57]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_60]),
                                static_cast<double>(glob->gv_promote_img[l_offp_61]),
                                static_cast<double>(glob->gv_promote_img[l_offp_62]),
                                static_cast<double>(glob->gv_promote_img[l_offp_63]),
                                static_cast<double>(glob->gv_promote_img[l_offp_64]),
                                static_cast<double>(glob->gv_promote_img[l_offp_65]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_68]),
                                static_cast<double>(glob->gv_promote_img[l_offp_69]),
                                static_cast<double>(glob->gv_promote_img[l_offp_70]),
                                static_cast<double>(glob->gv_promote_img[l_offp_71]),
                                static_cast<double>(glob->gv_promote_img[l_offp_72]),
                                static_cast<double>(glob->gv_promote_img[l_offp_73]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_76]),
                                static_cast<double>(glob->gv_promote_img[l_offp_77]),
                                static_cast<double>(glob->gv_promote_img[l_offp_78]),
                                static_cast<double>(glob->gv_promote_img[l_offp_79]),
                                static_cast<double>(glob->gv_promote_img[l_offp_80]),
                                static_cast<double>(glob->gv_promote_img[l_offp_81]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_83]),
                                static_cast<double>(glob->gv_promote_img[l_offp_84]),
                                static_cast<double>(glob->gv_promote_img[l_offp_85]),
                                static_cast<double>(glob->gv_promote_img[l_offp_86]),
                                static_cast<double>(glob->gv_promote_img[l_offp_87]),
                                static_cast<double>(glob->gv_promote_img[l_offp_88]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_90]),
                                static_cast<double>(glob->gv_promote_img[l_offp_91]),
                                static_cast<double>(glob->gv_promote_img[l_offp_92]),
                                static_cast<double>(glob->gv_promote_img[l_offp_93]),
                                static_cast<double>(glob->gv_promote_img[l_offp_94]),
                                static_cast<double>(glob->gv_promote_img[l_offp_95]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_97]),
                                static_cast<double>(glob->gv_promote_img[l_offp_98]),
                                static_cast<double>(glob->gv_promote_img[l_offp_99]),
                                static_cast<double>(glob->gv_promote_img[l_offp_100]),
                                static_cast<double>(glob->gv_promote_img[l_offp_101]),
                                static_cast<double>(glob->gv_promote_img[l_offp_102]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_104]),
                                static_cast<double>(glob->gv_promote_img[l_offp_105]),
                                static_cast<double>(glob->gv_promote_img[l_offp_106]),
                                static_cast<double>(glob->gv_promote_img[l_offp_107]),
                                static_cast<double>(glob->gv_promote_img[l_offp_108]),
                                static_cast<double>(glob->gv_promote_img[l_offp_109]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_111]),
                                static_cast<double>(glob->gv_promote_img[l_offp_112]),
                                static_cast<double>(glob->gv_promote_img[l_offp_113]),
                                static_cast<double>(glob->gv_promote_img[l_offp_114]),
                                static_cast<double>(glob->gv_promote_img[l_offp_115]),
                                static_cast<double>(glob->gv_promote_img[l_offp_116]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_119]),
                                static_cast<double>(glob->gv_promote_img[l_offp_120]),
                                static_cast<double>(glob->gv_promote_img[l_offp_121]),
                                static_cast<double>(glob->gv_promote_img[l_offp_122]),
                                static_cast<double>(glob->gv_promote_img[l_offp_123]),
                                static_cast<double>(glob->gv_promote_img[l_offp_124]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_126]),
                                static_cast<double>(glob->gv_promote_img[l_offp_127]),
                                static_cast<double>(glob->gv_promote_img[l_offp_128]),
                                static_cast<double>(glob->gv_promote_img[l_offp_129]),
                                static_cast<double>(glob->gv_promote_img[l_offp_130]),
                                static_cast<double>(glob->gv_promote_img[l_offp_131]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_133]),
                                static_cast<double>(glob->gv_promote_img[l_offp_134]),
                                static_cast<double>(glob->gv_promote_img[l_offp_135]),
                                static_cast<double>(glob->gv_promote_img[l_offp_136]),
                                static_cast<double>(glob->gv_promote_img[l_offp_137]),
                                static_cast<double>(glob->gv_promote_img[l_offp_138]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_140]),
                                static_cast<double>(glob->gv_promote_img[l_offp_141]),
                                static_cast<double>(glob->gv_promote_img[l_offp_142]),
                                static_cast<double>(glob->gv_promote_img[l_offp_143]),
                                static_cast<double>(glob->gv_promote_img[l_offp_144]),
                                static_cast<double>(glob->gv_promote_img[l_offp_145]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_147]),
                                static_cast<double>(glob->gv_promote_img[l_offp_148]),
                                static_cast<double>(glob->gv_promote_img[l_offp_149]),
                                static_cast<double>(glob->gv_promote_img[l_offp_150]),
                                static_cast<double>(glob->gv_promote_img[l_offp_151]),
                                static_cast<double>(glob->gv_promote_img[l_offp_152]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_154]),
                                static_cast<double>(glob->gv_promote_img[l_offp_155]),
                                static_cast<double>(glob->gv_promote_img[l_offp_156]),
                                static_cast<double>(glob->gv_promote_img[l_offp_157]),
                                static_cast<double>(glob->gv_promote_img[l_offp_158]),
                                static_cast<double>(glob->gv_promote_img[l_offp_159]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_162]),
                                static_cast<double>(glob->gv_promote_img[l_offp_163]),
                                static_cast<double>(glob->gv_promote_img[l_offp_164]),
                                static_cast<double>(glob->gv_promote_img[l_offp_165]),
                                static_cast<double>(glob->gv_promote_img[l_offp_166]),
                                static_cast<double>(glob->gv_promote_img[l_offp_167]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_169]),
                                static_cast<double>(glob->gv_promote_img[l_offp_170]),
                                static_cast<double>(glob->gv_promote_img[l_offp_171]),
                                static_cast<double>(glob->gv_promote_img[l_offp_172]),
                                static_cast<double>(glob->gv_promote_img[l_offp_173]),
                                static_cast<double>(glob->gv_promote_img[l_offp_174]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_176]),
                                static_cast<double>(glob->gv_promote_img[l_offp_177]),
                                static_cast<double>(glob->gv_promote_img[l_offp_178]),
                                static_cast<double>(glob->gv_promote_img[l_offp_179]),
                                static_cast<double>(glob->gv_promote_img[l_offp_180]),
                                static_cast<double>(glob->gv_promote_img[l_offp_181]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_183]),
                                static_cast<double>(glob->gv_promote_img[l_offp_184]),
                                static_cast<double>(glob->gv_promote_img[l_offp_185]),
                                static_cast<double>(glob->gv_promote_img[l_offp_186]),
                                static_cast<double>(glob->gv_promote_img[l_offp_187]),
                                static_cast<double>(glob->gv_promote_img[l_offp_188]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_190]),
                                static_cast<double>(glob->gv_promote_img[l_offp_191]),
                                static_cast<double>(glob->gv_promote_img[l_offp_192]),
                                static_cast<double>(glob->gv_promote_img[l_offp_193]),
                                static_cast<double>(glob->gv_promote_img[l_offp_194]),
                                static_cast<double>(glob->gv_promote_img[l_offp_195]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_197]),
                                static_cast<double>(glob->gv_promote_img[l_offp_198]),
                                static_cast<double>(glob->gv_promote_img[l_offp_199]),
                                static_cast<double>(glob->gv_promote_img[l_offp_200]),
                                static_cast<double>(glob->gv_promote_img[l_offp_201]),
                                static_cast<double>(glob->gv_promote_img[l_offp_202]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_205]),
                                static_cast<double>(glob->gv_promote_img[l_offp_206]),
                                static_cast<double>(glob->gv_promote_img[l_offp_207]),
                                static_cast<double>(glob->gv_promote_img[l_offp_208]),
                                static_cast<double>(glob->gv_promote_img[l_offp_209]),
                                static_cast<double>(glob->gv_promote_img[l_offp_210]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_212]),
                                static_cast<double>(glob->gv_promote_img[l_offp_213]),
                                static_cast<double>(glob->gv_promote_img[l_offp_214]),
                                static_cast<double>(glob->gv_promote_img[l_offp_215]),
                                static_cast<double>(glob->gv_promote_img[l_offp_216]),
                                static_cast<double>(glob->gv_promote_img[l_offp_217]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_219]),
                                static_cast<double>(glob->gv_promote_img[l_offp_220]),
                                static_cast<double>(glob->gv_promote_img[l_offp_221]),
                                static_cast<double>(glob->gv_promote_img[l_offp_222]),
                                static_cast<double>(glob->gv_promote_img[l_offp_223]),
                                static_cast<double>(glob->gv_promote_img[l_offp_224]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_226]),
                                static_cast<double>(glob->gv_promote_img[l_offp_227]),
                                static_cast<double>(glob->gv_promote_img[l_offp_228]),
                                static_cast<double>(glob->gv_promote_img[l_offp_229]),
                                static_cast<double>(glob->gv_promote_img[l_offp_230]),
                                static_cast<double>(glob->gv_promote_img[l_offp_231]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_233]),
                                static_cast<double>(glob->gv_promote_img[l_offp_234]),
                                static_cast<double>(glob->gv_promote_img[l_offp_235]),
                                static_cast<double>(glob->gv_promote_img[l_offp_236]),
                                static_cast<double>(glob->gv_promote_img[l_offp_237]),
                                static_cast<double>(glob->gv_promote_img[l_offp_238]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_240]),
                                static_cast<double>(glob->gv_promote_img[l_offp_241]),
                                static_cast<double>(glob->gv_promote_img[l_offp_242]),
                                static_cast<double>(glob->gv_promote_img[l_offp_243]),
                                static_cast<double>(glob->gv_promote_img[l_offp_244]),
                                static_cast<double>(glob->gv_promote_img[l_offp_245]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_248]),
                                static_cast<double>(glob->gv_promote_img[l_offp_249]),
                                static_cast<double>(glob->gv_promote_img[l_offp_250]),
                                static_cast<double>(glob->gv_promote_img[l_offp_251]),
                                static_cast<double>(glob->gv_promote_img[l_offp_252]),
                                static_cast<double>(glob->gv_promote_img[l_offp_253]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_255]),
                                static_cast<double>(glob->gv_promote_img[l_offp_256]),
                                static_cast<double>(glob->gv_promote_img[l_offp_257]),
                                static_cast<double>(glob->gv_promote_img[l_offp_258]),
                                static_cast<double>(glob->gv_promote_img[l_offp_259]),
                                static_cast<double>(glob->gv_promote_img[l_offp_260]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_262]),
                                static_cast<double>(glob->gv_promote_img[l_offp_263]),
                                static_cast<double>(glob->gv_promote_img[l_offp_264]),
                                static_cast<double>(glob->gv_promote_img[l_offp_265]),
                                static_cast<double>(glob->gv_promote_img[l_offp_266]),
                                static_cast<double>(glob->gv_promote_img[l_offp_267]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_269]),
                                static_cast<double>(glob->gv_promote_img[l_offp_270]),
                                static_cast<double>(glob->gv_promote_img[l_offp_271]),
                                static_cast<double>(glob->gv_promote_img[l_offp_272]),
                                static_cast<double>(glob->gv_promote_img[l_offp_273]),
                                static_cast<double>(glob->gv_promote_img[l_offp_274]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_276]),
                                static_cast<double>(glob->gv_promote_img[l_offp_277]),
                                static_cast<double>(glob->gv_promote_img[l_offp_278]),
                                static_cast<double>(glob->gv_promote_img[l_offp_279]),
                                static_cast<double>(glob->gv_promote_img[l_offp_280]),
                                static_cast<double>(glob->gv_promote_img[l_offp_281]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_283]),
                                static_cast<double>(glob->gv_promote_img[l_offp_284]),
                                static_cast<double>(glob->gv_promote_img[l_offp_285]),
                                static_cast<double>(glob->gv_promote_img[l_offp_286]),
                                static_cast<double>(glob->gv_promote_img[l_offp_287]),
                                static_cast<double>(glob->gv_promote_img[l_offp_288])))))));
        double l_vdot_306 = vdot6(v_298,
            vcons6(
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_23 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_25 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_27 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_29 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_31 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_33 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_36 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_37 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_38 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_39 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_40 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_41 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_44 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_45 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_46 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_47 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_48 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_49 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_52 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_53 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_54 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_55 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_56 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_57 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_60 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_61 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_62 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_63 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_64 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_65 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_68 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_69 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_70 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_71 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_72 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_73 + 1]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_76 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_77 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_78 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_79 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_80 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_81 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_83 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_84 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_85 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_86 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_87 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_88 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_90 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_91 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_92 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_93 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_94 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_95 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_97 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_98 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_99 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_100 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_101 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_102 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_104 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_105 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_106 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_107 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_108 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_109 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_111 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_112 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_113 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_114 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_115 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_116 + 1]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_119 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_120 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_121 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_122 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_123 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_124 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_126 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_127 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_128 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_129 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_130 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_131 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_133 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_134 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_135 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_136 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_137 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_138 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_140 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_141 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_142 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_143 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_144 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_145 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_147 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_148 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_149 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_150 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_151 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_152 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_154 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_155 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_156 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_157 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_158 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_159 + 1]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_162 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_163 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_164 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_165 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_166 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_167 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_169 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_170 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_171 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_172 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_173 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_174 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_176 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_177 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_178 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_179 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_180 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_181 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_183 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_184 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_185 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_186 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_187 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_188 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_190 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_191 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_192 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_193 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_194 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_195 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_197 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_198 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_199 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_200 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_201 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_202 + 1]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_205 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_206 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_207 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_208 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_209 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_210 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_212 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_213 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_214 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_215 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_216 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_217 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_219 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_220 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_221 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_222 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_223 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_224 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_226 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_227 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_228 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_229 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_230 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_231 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_233 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_234 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_235 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_236 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_237 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_238 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_240 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_241 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_242 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_243 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_244 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_245 + 1]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_248 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_249 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_250 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_251 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_252 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_253 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_255 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_256 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_257 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_258 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_259 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_260 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_262 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_263 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_264 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_265 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_266 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_267 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_269 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_270 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_271 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_272 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_273 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_274 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_276 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_277 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_278 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_279 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_280 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_281 + 1]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_283 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_284 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_285 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_286 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_287 + 1]),
                                static_cast<double>(glob->gv_promote_img[l_offp_288 + 1])))))));
        double l_vdot_307 = vdot6(v_298,
            vcons6(
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_23 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_25 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_27 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_29 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_31 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_33 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_36 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_37 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_38 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_39 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_40 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_41 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_44 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_45 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_46 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_47 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_48 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_49 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_52 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_53 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_54 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_55 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_56 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_57 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_60 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_61 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_62 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_63 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_64 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_65 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_68 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_69 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_70 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_71 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_72 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_73 + 2]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_76 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_77 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_78 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_79 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_80 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_81 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_83 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_84 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_85 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_86 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_87 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_88 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_90 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_91 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_92 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_93 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_94 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_95 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_97 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_98 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_99 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_100 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_101 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_102 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_104 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_105 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_106 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_107 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_108 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_109 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_111 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_112 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_113 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_114 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_115 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_116 + 2]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_119 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_120 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_121 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_122 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_123 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_124 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_126 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_127 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_128 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_129 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_130 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_131 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_133 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_134 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_135 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_136 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_137 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_138 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_140 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_141 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_142 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_143 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_144 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_145 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_147 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_148 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_149 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_150 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_151 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_152 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_154 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_155 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_156 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_157 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_158 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_159 + 2]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_162 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_163 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_164 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_165 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_166 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_167 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_169 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_170 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_171 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_172 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_173 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_174 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_176 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_177 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_178 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_179 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_180 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_181 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_183 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_184 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_185 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_186 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_187 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_188 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_190 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_191 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_192 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_193 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_194 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_195 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_197 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_198 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_199 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_200 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_201 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_202 + 2]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_205 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_206 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_207 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_208 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_209 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_210 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_212 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_213 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_214 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_215 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_216 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_217 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_219 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_220 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_221 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_222 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_223 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_224 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_226 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_227 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_228 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_229 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_230 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_231 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_233 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_234 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_235 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_236 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_237 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_238 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_240 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_241 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_242 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_243 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_244 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_245 + 2]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_248 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_249 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_250 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_251 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_252 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_253 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_255 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_256 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_257 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_258 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_259 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_260 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_262 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_263 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_264 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_265 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_266 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_267 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_269 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_270 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_271 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_272 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_273 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_274 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_276 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_277 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_278 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_279 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_280 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_281 + 2]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_283 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_284 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_285 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_286 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_287 + 2]),
                                static_cast<double>(glob->gv_promote_img[l_offp_288 + 2])))))));
        double l_vdot_308 = vdot6(v_298,
            vcons6(
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_23 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_25 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_27 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_29 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_31 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_33 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_36 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_37 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_38 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_39 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_40 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_41 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_44 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_45 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_46 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_47 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_48 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_49 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_52 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_53 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_54 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_55 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_56 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_57 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_60 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_61 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_62 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_63 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_64 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_65 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_68 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_69 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_70 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_71 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_72 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_73 + 3]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_76 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_77 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_78 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_79 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_80 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_81 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_83 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_84 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_85 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_86 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_87 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_88 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_90 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_91 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_92 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_93 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_94 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_95 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_97 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_98 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_99 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_100 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_101 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_102 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_104 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_105 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_106 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_107 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_108 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_109 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_111 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_112 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_113 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_114 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_115 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_116 + 3]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_119 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_120 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_121 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_122 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_123 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_124 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_126 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_127 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_128 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_129 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_130 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_131 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_133 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_134 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_135 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_136 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_137 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_138 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_140 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_141 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_142 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_143 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_144 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_145 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_147 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_148 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_149 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_150 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_151 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_152 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_154 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_155 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_156 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_157 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_158 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_159 + 3]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_162 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_163 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_164 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_165 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_166 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_167 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_169 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_170 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_171 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_172 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_173 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_174 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_176 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_177 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_178 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_179 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_180 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_181 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_183 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_184 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_185 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_186 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_187 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_188 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_190 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_191 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_192 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_193 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_194 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_195 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_197 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_198 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_199 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_200 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_201 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_202 + 3]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_205 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_206 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_207 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_208 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_209 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_210 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_212 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_213 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_214 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_215 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_216 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_217 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_219 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_220 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_221 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_222 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_223 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_224 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_226 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_227 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_228 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_229 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_230 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_231 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_233 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_234 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_235 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_236 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_237 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_238 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_240 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_241 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_242 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_243 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_244 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_245 + 3]))))),
                vdot6(v_301,
                    vcons6(
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_248 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_249 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_250 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_251 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_252 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_253 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_255 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_256 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_257 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_258 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_259 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_260 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_262 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_263 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_264 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_265 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_266 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_267 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_269 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_270 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_271 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_272 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_273 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_274 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_276 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_277 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_278 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_279 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_280 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_281 + 3]))),
                        vdot6(v_304,
                            vcons6(static_cast<double>(glob->gv_promote_img[l_offp_283 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_284 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_285 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_286 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_287 + 3]),
                                static_cast<double>(glob->gv_promote_img[l_offp_288 + 3])))))));
        double l_r_309 = tensor_ref_2_2(glob->gv_F0)[0];
        double l_r_310 = tensor_ref_2_2(glob->gv_F0)[1];
        double l_r_311 = tensor_ref_2_2(glob->gv_F0)[2];
        double l_r_312 = tensor_ref_2_2(glob->gv_F0)[3];
        l_out_313[0] = l_r_309 * l_vdot_305;
        l_out_313[1] = l_r_309 * l_vdot_306;
        l_out_313[2] = l_r_309 * l_vdot_307;
        l_out_313[3] = l_r_309 * l_vdot_308;
        l_out_313[4] = l_r_310 * l_vdot_305;
        l_out_313[5] = l_r_310 * l_vdot_306;
        l_out_313[6] = l_r_310 * l_vdot_307;
        l_out_313[7] = l_r_310 * l_vdot_308;
        l_out_313[8] = l_r_311 * l_vdot_305;
        l_out_313[9] = l_r_311 * l_vdot_306;
        l_out_313[10] = l_r_311 * l_vdot_307;
        l_out_313[11] = l_r_311 * l_vdot_308;
        l_out_313[12] = l_r_312 * l_vdot_305;
        l_out_313[13] = l_r_312 * l_vdot_306;
        l_out_313[14] = l_r_312 * l_vdot_307;
        l_out_313[15] = l_r_312 * l_vdot_308;
    }
    else {
        l_out_313[0] = 0.72e1;
        l_out_313[1] = 0.72e1;
        l_out_313[2] = 0.72e1;
        l_out_313[3] = 0.72e1;
        l_out_313[4] = 0.72e1;
        l_out_313[5] = 0.72e1;
        l_out_313[6] = 0.72e1;
        l_out_313[7] = 0.72e1;
        l_out_313[8] = 0.72e1;
        l_out_313[9] = 0.72e1;
        l_out_313[10] = 0.72e1;
        l_out_313[11] = 0.72e1;
        l_out_313[12] = 0.72e1;
        l_out_313[13] = 0.72e1;
        l_out_313[14] = 0.72e1;
        l_out_313[15] = 0.72e1;
    }
    self->sv_out = l_out_313;
    return diderot::kStabilize;
}
bool output_get_out (world *wrld, Nrrd *nData)
{
    // Compute sizes of nrrd file
    size_t sizes[2];
    sizes[0] = 16;
    sizes[1] = wrld->_size[0];
    // Allocate nData nrrd
    if (nrrdMaybeAlloc_nva(nData, nrrdTypeDouble, 2, sizes) != 0) {
        char *msg = biffGetDone(NRRD);
        biffMsgAdd(wrld->_errors, msg);
        std::free(msg);
        return true;
    }
    // copy data to output nrrd
    char *cp = reinterpret_cast<char *>(nData->data);
    for (auto ix = wrld->_strands.begin_alive(); ix != wrld->_strands.end_alive(); ix = wrld->_strands.next_alive(ix)) {
        memcpy(cp, &wrld->_strands.strand(ix)->sv_out, 16 * sizeof(double));
        cp += 16 * sizeof(double);
    }
    nData->axis[0].kind = nrrdKindList;
    nData->axis[1].kind = nrrdKindSpace;
    return false;
}
static void write_output (world *wrld)
{
    Nrrd *nData;
    nData = nrrdNew();
    if (output_get_out(wrld, nData)) {
        std::cerr << "Error getting nrrd data:\n" << biffMsgStrGet(wrld->_errors) << std::endl;
        delete wrld;
        exit(1);
    }
    else if (nrrd_save_helper(OutputFile, nData)) {
        exit(1);
    }
    nrrdNuke(nData);
}
/*---------- begin world-methods.in ----------*/
// Allocate the program's world
//
world::world ()
    : diderot::world_base (ProgramName, true, 1)
{
#ifndef DIDEROT_NO_GLOBALS
    this->_globals = new globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = nullptr;
#endif
} // world constructor

// shutdown and deallocate the world
//
world::~world ()
{
#ifndef DIDEROT_NO_GLOBALS
    delete this->_globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    delete this->_tree;
#endif

} // world destructor

// Initialize the program's world
//
bool world::init ()
{
    assert (this->_stage == diderot::POST_NEW);

#if !defined(DIDEROT_STANDALONE_EXEC) && !defined(DIDEROT_NO_INPUTS)
  // initialize the defined flags for the input globals
    init_defined_inputs (this);
#endif

#ifdef DIDEROT_TARGET_PARALLEL
  // get CPU info
    if (this->_sched->get_cpu_info (this)) {
        return true;
    }
#endif

    this->_stage = diderot::POST_INIT;

    return false;

}

// allocate the initial strands and initialize the rest of the world structure.
//
bool world::alloc (int32_t base[1], uint32_t size[1])
{
    size_t numStrands = 1;
    for (uint32_t i = 0;  i < 1;  i++) {
        numStrands *= size[i];
        this->_base[i] = base[i];
        this->_size[i] = size[i];
    }

    if (this->_verbose) {
        std::cerr << "world::alloc: " << size[0];
        for (uint32_t i = 1;  i < 1;  i++) {
            std::cerr << " x " << size[i];
        }
        std::cerr << std::endl;
    }

#ifdef DIDEROT_TARGET_PARALLEL
  // determine the block size based on the initial number of strands and the
  // number of workers
    this->_strands.set_block_size (this->_sched->_numWorkers, numStrands);
#endif

  // allocate the strand array
    if (this->_strands.alloc (numStrands)) {
        biffMsgAdd (this->_errors, "unable to allocate strand-state array\n");
        return true;
    }

  // initialize strand state pointers etc.
    this->_strands.create_strands (numStrands);

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = new diderot::kdtree<0, double, strand_array> (&this->_strands);
#endif

    return false;

} // world::alloc

// swap input and output states
//
inline void world::swap_state ()
{
    this->_strands.swap ();
}

#ifdef DIDEROT_HAS_KILL_ALL
void world::kill_all ()
{
    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            ix = this->_strands.kill (ix);
        }
        this->_strands.finish_kill_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif

#ifdef DIDEROT_HAS_STABILIZE_ALL
void world::stabilize_all ()
{
#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            this->_strands._status[ix] = diderot::kStable;
            ix = this->_strands.strand_stabilize (ix);
        }
        this->_strands.finish_stabilize_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif
/*---------- end world-methods.in ----------*/

bool world::create_strands ()
{
    if (init_globals(this)) {
        return true;
    }
    globals *glob = this->_globals;
    int lo_0 = 0;
    int hi_1 = glob->gv_length;
    int32_t base[1] = {lo_0,};
    uint32_t size[1] = {static_cast<uint32_t>(hi_1 - lo_0 + 1),};
    if (this->alloc(base, size)) {
        return true;
    }
    uint32_t ix = 0;
    for (int i_i_314 = lo_0; i_i_314 <= hi_1; i_i_314++) {
        f_init(this->_strands.strand(ix), i_i_314);
        ++ix;
    }
    this->swap_state();
    this->_stage = diderot::POST_CREATE;
    return false;
}
/*---------- begin seq-run-nobsp.in ----------*/
//! Run the Diderot program (sequential version without BSP semantics)
//! \param max_nsteps the limit on the number of super steps; 0 means unlimited
//! \return the number of steps taken, or 0 on error.
uint32_t world::run (uint32_t max_nsteps)
{
    if (this->_stage == diderot::POST_CREATE) {
#ifdef DIDEROT_HAS_GLOBAL_START
        this->global_start();
#endif
        this->_stage = diderot::RUNNING;
    }
    assert (this->_stage == diderot::RUNNING);

#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (max_nsteps == 0) {
        max_nsteps = 0xffffffff;  // essentially unlimited
    }

    double t0 = airTime();

    if (this->_verbose) {
        std::cerr << "run with " << this->_strands.num_alive() << " strands ..." << std::endl;
    }

#ifdef DIDEROT_HAS_START_METHOD
    this->run_start_methods();
#endif

  // iterate until all strands are stable
    uint32_t maxSteps = 0;
    for (auto ix = this->_strands.begin_active();
         ix != this->_strands.end_active();
         )
    {
        diderot::strand_status sts = this->_strands.status(ix);
        uint32_t nSteps = 0;
        while ((! sts) && (nSteps < max_nsteps)) {
            nSteps++;
            sts = this->_strands.strand_update(glob, ix);
        }
        switch (sts) {
          case diderot::kStabilize:
          // stabilize the strand's state.
            ix = this->_strands.strand_stabilize (ix);
            break;
#ifdef DIDEROT_HAS_STRAND_DIE
          case diderot::kDie:
            ix = this->_strands.kill (ix);
            break;
#endif
          default:
            assert (sts == this->_strands.status(ix));
	    ix = this->_strands.next_active(ix);
            break;
        }
        if (maxSteps < nSteps) maxSteps = nSteps;
    }

    this->_run_time += airTime() - t0;

    if (this->_strands.num_active() == 0)
        this->_stage = diderot::DONE;

    return maxSteps;

} // world::run
/*---------- end seq-run-nobsp.in ----------*/

/*---------- begin namespace-close.in ----------*/

} // namespace Diderot
/*---------- end namespace-close.in ----------*/

/*---------- begin seq-main.in ----------*/
using namespace Diderot;

//! Main function for standalone sequential C target
//
int main (int argc, const char **argv)
{
    bool        timingFlg = false;      //! true if timing computation
    uint32_t    stepLimit = 0;          //! limit on number of execution steps (0 means unlimited)
    std::string printFile = "-";        //! file to direct printed output into
#ifdef DIDEROT_EXEC_SNAPSHOT
    uint32_t    snapshotPeriod = 0;     //! supersteps per snapshot; 0 means no snapshots
#endif
    uint32_t    nSteps = 0;             //! number of supersteps taken

  // create the world
    world *wrld = new (std::nothrow) world();
    if (wrld == nullptr) {
        std::cerr << "unable to create world" << std::endl;
        exit(1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the default values for the inputs
    cmd_line_inputs inputs;
    init_defaults (&inputs);
#endif

  // handle command-line options
    {
        diderot::options *opts = new diderot::options ();
        opts->add ("l,limit", "specify limit on number of super-steps (0 means unlimited)",
            &stepLimit, true);
#ifdef DIDEROT_EXEC_SNAPSHOT
        opts->add ("s,snapshot",
            "specify number of super-steps per snapshot (0 means no snapshots)",
            &snapshotPeriod, true);
#endif
        opts->add ("print", "specify where to direct printed output", &printFile, true);
        opts->addFlag ("v,verbose", "enable runtime-system messages", &(wrld->_verbose));
        opts->addFlag ("t,timing", "enable execution timing", &timingFlg);
#ifndef DIDEROT_NO_INPUTS
      // register options for setting global inputs
        register_inputs (&inputs, opts);
#endif
        register_outputs (opts);
        opts->process (argc, argv);
        delete opts;
    }

  // redirect printing (if necessary)
    if (printFile.compare("-") != 0) {
        wrld->_printTo = new std::ofstream (printFile);
        if (wrld->_printTo->fail()) {
            std::cerr << "Error opening print file" << std::endl;
            delete wrld;
            exit(1);
        }
    }

  // initialize scheduler stuff
    if (wrld->_verbose) {
        std::cerr << "initializing world ..." << std::endl;
    }
    if (wrld->init()) {
        std::cerr << "Error initializing world:\n" << wrld->get_errors() << std::endl;
        delete wrld;
        exit(1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the input globals
    if (init_inputs (wrld, &inputs)) {
        std::cerr << "Error initializing inputs:\n" << wrld->get_errors() << std::endl;
        delete wrld;
        exit(1);
    }
#endif

  // run the generated global initialization code
    if (wrld->_verbose) {
        std::cerr << "initializing globals and creating strands ...\n";
    }
    if (wrld->create_strands()) {
        std::cerr << "Error in global initialization:\n"
            << wrld->get_errors() << std::endl;
        delete wrld;
        exit(1);
    }

#ifdef DIDEROT_EXEC_SNAPSHOT

    if (snapshotPeriod > 0) {
     // write initial state as snapshot 0
        write_snapshot (wrld, "-0000");
     // run the program for `snapshotPeriod` steps at a time with a snapshot after each run
        while (true) {
            uint32_t n, limit;
          // determine a step limit for the next run
            if (stepLimit > 0) {
                if (stepLimit <= nSteps) {
                    break;
                }
                limit = std::min(stepLimit - nSteps, snapshotPeriod);
            }
            else {
                limit = snapshotPeriod;
            }
          // run the program for upto limit steps
            if ((n = wrld->run (limit)) == 0) {
                break;
            }
            nSteps += n;
            if ((wrld->_errors->errNum > 0) || (wrld->_strands.num_alive() == 0)) {
                break;
            }
          // write a snapshot with the step count as a suffix
            std::string suffix = std::to_string(nSteps);
            if (suffix.length() < 4) {
                suffix = std::string("0000").substr(0, 4 - suffix.length()) + suffix;
            }
            suffix = "-" + suffix;
            write_snapshot (wrld, suffix);
        }
    }
    else {
        nSteps = wrld->run (stepLimit);
    }

#else // !DIDEROT_EXEC_SNAPSHOT

    nSteps = wrld->run (stepLimit);

#endif // DIDEROT_EXEC_SNAPSHOT

    if (wrld->_errors->errNum > 0) {
        std::cerr << "Error during execution:\n" << wrld->get_errors() << std::endl;
        delete wrld;
        exit(1);
    }

    if ((stepLimit != 0) && (wrld->_strands.num_active() > 0)) {
#ifdef DIDEROT_STRAND_ARRAY
        if (wrld->_verbose) {
            std::cerr << "Step limit expired; "
                << wrld->_strands.num_active() << " active strands remaining" << std::endl;
        }
#else
      // step limit expired, so kill remaining strands
        if (wrld->_verbose) {
            std::cerr << "Step limit expired. Killing remaining "
                << wrld->_strands.num_active() << " active strands" << std::endl;
        }
        wrld->kill_all();
#endif
    }

    if (wrld->_verbose) {
        std::cerr << "done: " << nSteps << " steps, in " << wrld->_run_time << " seconds";
#ifndef DIDEROT_STRAND_ARRAY
        std::cerr << "; " << wrld->_strands.num_stable() << " stable strands" << std::endl;
#else
        std::cerr << std::endl;
#endif
    }
    else if (timingFlg) {
        std::cout << "usr=" << wrld->_run_time << std::endl;
    }

  // output the final strand states
    write_output (wrld);

    delete wrld;

    return 0;

} // main
/*---------- end seq-main.in ----------*/

